import os
import pkg_resources
from mako.lookup import TemplateLookup
from formbar.config import Config, load
from formbar.form import Form

from ringo.lib.helpers import (
    get_item_modul
)
from ringo.lib.form import (
    eval_url,
    get_path_to_form_config,
)
from ringo.lib.renderer.dialogs import DialogRenderer

base_dir = pkg_resources.get_distribution("ringo_printtemplates").location
template_dir = os.path.join(base_dir, 'ringo_printtemplates', 'templates')
template_lookup = TemplateLookup(directories=[template_dir])


class PrintDialogRenderer(DialogRenderer):
    """Docstring for ImportDialogRenderer"""

    def __init__(self, request, clazz):
        """@todo: to be defined """
        DialogRenderer.__init__(self, request, clazz, "print")
        self.template = template_lookup.get_template("print.mako")
        config = Config(load(get_path_to_form_config('print.xml',
                                                     'ringo_printtemplates')))
        form_config = config.get_form('default')
        self.form = Form(form_config,
                         item=clazz,
                         csrf_token=self._request.session.get_csrf_token(),
                         dbsession=request.db,
                         eval_url=eval_url,
                         url_prefix=request.application_url)

    def render(self):
        values = {}
        values['request'] = self._request
        values['body'] = self._render_body()
        values['modul'] = get_item_modul(self._request,
                                         self._item).get_label(plural=True)
        values['action'] = self._action.capitalize()
        values['ok_url'] = self._request.current_route_path()
        values['_'] = self._request.translate
        values['cancel_url'] = self._request.referrer
        values['eval_url'] = self._request.application_url + eval_url
        return self.template.render(**values)

    def _render_body(self):
        out = []
        out.append(self.form.render(buttons=False))
        return "".join(out)

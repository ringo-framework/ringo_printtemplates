import os
import pkg_resources
from mako.lookup import TemplateLookup
from formbar.config import Config, load
from formbar.form import Form

import ringo.lib.helpers
from ringo.lib.helpers import (
    get_item_modul,
    get_app_url,
    literal
)
from ringo.lib.form import (
    get_eval_url,
    get_path_to_form_config,
)
from ringo.lib.renderer.dialogs import DialogRenderer
from ringo_printtemplate.model import Printtemplate

base_dir = pkg_resources.get_distribution("ringo_printtemplate").location
template_dir = os.path.join(base_dir, 'ringo_printtemplate', 'templates')
template_lookup = TemplateLookup(directories=[template_dir],
                                 default_filters=['h'])


class PrintDialogRenderer(DialogRenderer):
    """Docstring for ImportDialogRenderer"""

    def __init__(self, request, clazz):
        """@todo: to be defined """
        DialogRenderer.__init__(self, request, clazz, "print")
        self.template = template_lookup.get_template("internal/print.mako")
        config = Config(load(get_path_to_form_config('print.xml',
                                                     'ringo_printtemplate',
                                                     '.')))
        form_config = config.get_form('default')
        # Load available_printtemplates and put them into the form as
        # external data. This than later used to render the available
        # printtemplates.
        mid = clazz._modul_id
        values = {}
        values['printtemplates'] = [(p, p.id) for p in self._item.printtemplates]
        self.form = Form(form_config,
                         item=clazz,
                         csrf_token=self._request.session.get_csrf_token(),
                         dbsession=request.db,
                         translate=request.translate,
                         url_prefix=get_app_url(request),
                         eval_url=get_eval_url(),
                         values=values)

    def render(self):
        modul = get_item_modul(self._request, self._item)
        template_modul = get_item_modul(self._request, Printtemplate)
        values = {}
        values['request'] = self._request
        values['body'] = self._render_body()
        values['modul'] = modul.get_label(plural=True)
        values['header'] = template_modul.get_label(plural=True)
        values['action'] = self._action.capitalize()
        values['ok_text'] = template_modul.get_label(plural=False)
        values['ok_url'] = self._request.current_route_path()
        values['_'] = self._request.translate
        values['cancel_url'] = self._request.ringo.history.last() or self._request.url.replace("print", "read")
        values['eval_url'] = self.form._eval_url
        values['h'] = ringo.lib.helpers
        return literal(self.template.render(**values))

    def _render_body(self):
        out = []
        out.append(self.form.render(buttons=False))
        return literal("").join(out)

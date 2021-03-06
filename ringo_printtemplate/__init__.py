import logging
from pyramid.i18n import TranslationStringFactory
from pyramid.config import Configurator
from ringo.lib.i18n import translators
from ringo.lib.extension import register_modul

# Import models so that alembic is able to autogenerate migrations
# scripts.
from ringo_printtemplate.model import Printtemplate
from ringo_printtemplate.server import setup_server

# This import is needed to trigger "registering" the views.
import ringo_printtemplate.views

log = logging.getLogger(__name__)

modul_config = {
    "name": "printtemplates",
    "label": "",
    "clazzpath": "ringo_printtemplate.model.Printtemplate",
    "label_plural": "",
    "str_repr": "",
    "display": "",
    "actions": ["list", "read", "update", "create", "delete", "download"]
}


def main(global_config, **settings):
    """ Will start the converter server.
    """
    config = Configurator(settings=settings)
    config = setup_server(config, global_config.get("oo_python"), global_config.get("oo_port"))
    return config.make_wsgi_app()


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    modul = register_modul(config, modul_config)
    if modul:
        Printtemplate._modul_id = modul.get_value("id")
        translators.append(TranslationStringFactory('ringo_printtemplate'))
        config.add_translation_dirs('ringo_printtemplate:locale/')
        config.add_route('printtemplates-print', '/printtemplates/print/{id}')
        config.include('ringo_printtemplate.odfconv.setup')
        config.scan()

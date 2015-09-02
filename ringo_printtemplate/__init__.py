import logging
from pyramid.i18n import TranslationStringFactory
from ringo.lib.i18n import translators
from ringo.lib.extension import register_modul

# Import models so that alembic is able to autogenerate migrations
# scripts.
from ringo_printtemplate.model import Printtemplate

log = logging.getLogger(__name__)

modul_config = {
    "name": "printtemplate",
    "label": "",
    "clazzpath": "ringo_printtemplate.model.Printtemplate",
    "label_plural": "",
    "str_repr": "",
    "display": "",
    "actions": ["list", "read", "update", "create", "delete", "download"]
}


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    modul = register_modul(config, modul_config)
    Printtemplate._modul_id = modul.get_value("id")
    translators.append(TranslationStringFactory('ringo_printtemplate'))
    config.add_translation_dirs('ringo_printtemplate:locale/')

import os
import base64
import requests
from tempfile import NamedTemporaryFile
import logging
from ringo.lib.cache import CACHE_MISC

log = logging.getLogger(__name__)


def setup(config):
    settings = config.registry.settings
    pythonpath = settings.get('converter.python')
    port = settings.get('converter.port', 2002)
    url = settings.get('converter.url')
    if settings.get('converter.start') == 'true':
        if url:
            converter = WebConverter(url=url)
            converter.start()
        else:
            converter = Converter(python=pythonpath, port=port, url=url)
            converter.start()
        CACHE_MISC.set("converter", converter)


def get_converter():
    return CACHE_MISC.get("converter")


class Converter(object):

    """Converter to convert ODF documents into other formats like pdf,
    xls, doc."""

    def __init__(self, python=None, port=None, url=None):
        from py3o.renderers.pyuno.main import Convertor
        self._converter = Convertor(python=python, port=port)

    def start(self):
        try:
            self._converter._init_server()
            log.info("Office Server for document conversation started.")
        except:
            log.exception("Office not started. Converter is not"
                          "available. Forgot to install Libreoffice?")

    def is_available(self):
        if not self._converter.server.is_running():
            self.start()
            return False
        return True

    def _get_infile(self, data):
        infile = NamedTemporaryFile()
        # Make file world readable. This prevents errors when other
        # users trying to use the converter.
        os.chmod(infile.name, 0o666)
        infile.write(data)
        infile.seek(0)
        return infile

    def convert(self, data, format="ods", update=True):
        """Returns the infile into the given format.

        :data: Loaded data from the source file
        :format: String of the output format
        :returns: Converted data.

        """
        infile = self._get_infile(data)
        outfile = NamedTemporaryFile()
        os.chmod(outfile.name, 0o666)
        # Update needs a patch
        #self._converter.convert(infile.name, outfile.name, format, update)
        self._converter.convert(infile.name, outfile.name, format)
        result = outfile.read()
        infile.close()
        outfile.close()
        return result


class WebConverter(Converter):

    def __init__(self, url):
        self._url = url

    def start(self):
        try:
            self.is_available()
            log.info("WebConverter for document conversation available.")
        except:
            log.exception("Office not started. Converter is not"
                          "available. Forgot to install Libreoffice?")

    def is_available(self):
        result = requests.get(self._url)
        return result.status_code == 200

    def convert(self, data, format="pdf", update=True):
        url = self._url + "/{}".format(format)
        data = {'odt': base64.b64encode(data)}
        result = requests.post(url, data=data)
        return base64.b64decode(result.content)

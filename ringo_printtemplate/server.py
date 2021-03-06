import base64
import logging
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from ringo_printtemplate.odfconv import Converter

CONVERTER = None
log = logging.getLogger(__name__)

def ping(request):
    return Response("Pong!")

def convert(request):
    if not request.POST:
       response = Response("Only POST request are allowed")
       response.status_code = 400
       return response
    else:
        data = base64.b64decode(request.POST.get("odt"))
        if not data:
            response = Response("Missing ODT content in data.")
            response.status_code = 400
            return response
        try:
            converted = CONVERTER.convert(data, format=request.matchdict.get("format"))
            return Response(base64.b64encode(converted))
        except Exception as e:
            log.exception(e)
            response = Response("Conversion failed.")
            response.status_code = 400
            return response

def run(host='0.0.0.0', port=5000, oopython='/usr/bin/python', ooport=2001):
    config = Configurator()
    config = setup_server(config, oopython, ooport)
    app = config.make_wsgi_app()
    server = make_server(host, port, app)
    print("Office for convertsion started.")
    print("Running Server on {}:{}.".format(host, port))
    server.serve_forever()

def setup_server(config, oopython='/usr/bin/python', ooport=2001):
    global CONVERTER
    config.add_route('ping', '/')
    config.add_route('convert', '/{format}')
    config.add_view(ping, route_name='ping')
    config.add_view(convert, route_name='convert')
    CONVERTER = Converter(oopython, ooport)
    CONVERTER.start()
    return config

if __name__ == '__main__':
    run()

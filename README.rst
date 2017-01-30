ringo_printtemplates
====================
This is a extionsion for the Ringo webframework. It can be used to save so
called printtemplates in the applications. Printtemplates are ODT Files which
can be filled with data comming from the module.

Template files are saved in the database on default, but using a special 
notation in the `data` field of the template model allows to refer to files
in the local filesystem too::

        @package:path/to/file/relative/to/package/file
        
Where package is the name of the application.

Optionally you can convert the ODT files into PDF. Therefor a libreoffice
installation must be running on the server.

The following configuation variables are available::

        ###
        # Settings for the Converter
        ###
        # Should the converter be started on application start? Set to
        # true to enable converter startup.
        converter.start = false
        # Set python path for the Converter. Defaults to the system python
        converter.python = /usr/bin/python3
        # Set port of which the client listen. Defaults to 2002
        converter.port = 2002
        # Instead of directly talking to the office you can talk to a
        # webservice.
        converter.url = http://127.0.0.1:5000

Webservice
----------
This extension comes with a small webservice which will take a ODT
document and return a converted document.

Do not fortget to configure your application to use this service.

ringo-odfconverter
^^^^^^^^^^^^^^^^^^
To start the service invoke the following command::

    ringo-odfconverter

The service will listen on `http://127.0.0.1:5000` on default. The service can
be "pinged" to check its availablilty on "/" url. It should return "Pong" with
status code 200.

Conversion of documents can be done by invoking a POST request on the server
with a base64 encoded `odt` file in the request POST params on
`http://127.0.0.1:5000/pdf`. The server will return a base64 encoded PDF
document.

pserve
^^^^^^
You can also start the application as a normal pyramid application using the
pserve command::

        pserve --reload development


Requirements
------------
If you encounter the following message on installation::

        ERROR: /bin/sh: xslt-config: Kommando nicht gefunden
        ** make sure the development packages of libxml2 and libxslt are installed **

You need to install the following packages if you want to compile lxml for
yourself::

        apt-get install libxml2-dev libxslt1-dev

An alternative might be to install lxml globally on your system and give your
virtual environment access to it.

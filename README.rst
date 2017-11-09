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

Optionally you can convert the ODT files into PDF. Therefore a libreoffice
installation must be installed on the server. Please also note that
currently (March 2017) the py3o.renderers.pyuno installation pulled by
setup.py seems to be broken. A workaround is manually installing the package
('pip install py3o.renderers.pyuno') before installing ringo_printtemplates.

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

License
-------
Ringo is Free Software. It is licensed under the GPL license in version 2 or
later. See `<http://www.gnu.org/licenses/gpl-2.0>`_ for more details on the license.

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

If you get the following message when trying to convert::

        ImportError: No module named uno

This is very likley the reason that you are running in python2 and your
libreoffice was build against python3. 

If you get the following error when trying to convert::

        OfficeException: Spawned client had an error: /usr/bin/python: can't find '__main__' module in '/home/torsten/Entwicklung/ringo-apps/speq/esf/env/lib/python2.7/site-packages/py3o.renderers.pyuno-0.5-py2.7.egg/py3o/renderers/pyuno/office.py

This is because the installed py3o.renderers.pyuno version which was installed
as a dependency seems to be broken. For me it helps to uninstall and reinstall
the library using pip::

        pip uninstall py3o.renderers.pyuno
        pip install py3o.renderers.pyuno

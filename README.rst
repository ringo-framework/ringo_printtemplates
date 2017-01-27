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

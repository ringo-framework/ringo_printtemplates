ringo_printtemplates
====================
This is a extionsion for the Ringo webframework. It can be used to save so
called printtemplates in the applications. Printtemplates are ODT Files which
can be filled with data comming from the module.

Optionally you can convert the ODT files into PDF. Therefor a libreoffice
installation must be running on the server.

The following configuation variables are available

..
        ###
        # Settings for the Converter
        ###
        # Should the converter be started on application start? Set to
        # true to enable converter startup.
        converter.start = false
        # Set python path for the Converter. Defaults to the system python
        converter.python = /usr/bin/python3

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '1.2'

setup(name='ringo_printtemplate',
      version=version,
      description="Extension for printtemplates in the ringo webframework",
      long_description="""This is a extension for the ringo framework. It allows you to upload printtemplate which can pe prefilled with data of an item for later printing.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ringo pyramid extension',
      author='Torsten Irländer',
      author_email='torsten.irlaender@googlemail.com',
      url='https://github.com/ringo-framework/ringo_printtemplates',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ringo',
          'py3o.template',
          'py3o.renderers.pyuno',
          'genshi'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [babel.extractors]
      tableconfig = ringo.lib.i18n:extract_i18n_tableconfig
      formconfig = formbar.i18n:extract_i18n_formconfig
      """,
      message_extractors = {'ringo_printtemplate': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('**.xml', 'formconfig', None),
            ('**.json', 'tableconfig', None),
            ('static/**', 'ignore', None)]},
      )

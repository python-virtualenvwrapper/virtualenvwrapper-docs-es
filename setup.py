#!/usr/bin/env python

PROJECT = 'virtualenvwrapper'

# Change docs/sphinx/conf.py too!
VERSION = '3.5'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

try:
    long_description = open('README.txt', 'rt').read()
except IOError:
    long_description = ''

setup(
    name = PROJECT,
    version = VERSION,
    
    description = 'Enhancements to virtualenv',
    long_description = long_description,
    
    author = 'Doug Hellmann',
    author_email = 'doug.hellmann@gmail.com',

    url = 'http://www.doughellmann.com/projects/%s/' % PROJECT,
    #download_url = 'http://www.doughellmann.com/downloads/%s-%s.tar.gz' % \
    #                (PROJECT, VERSION),

    classifiers = [ 'Development Status :: 5 - Production/Stable',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.6',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.2',
                    'Intended Audience :: Developers',
                    'Environment :: Console',
                    ],

    platforms = ['Any'],

    provides=['virtualenvwrapper_docs_es',
              ],

    packages = [],
    include_package_data = True,

    zip_safe=False,
    )

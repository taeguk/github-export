#-*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import sys

if sys.version_info.major < 3:
    msg = "Sorry, Python 2 is not supported (yet)"
    print >> sys.stderr, msg
    sys.exit(1)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup (
    name = 'github-export',
    version = '0.0.3',

    author = 'taeguk',
    author_email = 'xornrbboy@gmail.com',
    
    url = 'https://github.com/taeguk/github-export',
    license='MIT',
    description = "Export your github repositories.",
    long_description = long_description,
    
    packages=find_packages(),
    scripts=['bin/github-export'],
    include_package_data = True,

    install_requires = ['requests', 'gitpython'],

    classifiers = [
        'Programming Language :: Python :: 3 :: Only',
    ],
    
    keywords = 'github backup export repository',
)

#!/usr/bin/env python
from distutils.core import setup
from distutils.dir_util import copy_tree
import os


setup(
    name='mkproject',
    version='1.0',
    author='Will Boyce',
    author_email='me@willboyce.com',
    url='http://github.com/wrboyce/mkproject',
    py_modules=['mkproject'],
    scripts=['bin/mkproject'],
)
copy_tree(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates'), '/etc/mkproject/')

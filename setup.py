#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
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
    entry_points = { 
    'console_scripts':[
        'mkproject = mkproject:main'
    ]},  
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Licence :: BSD',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
    ]
)
copy_tree(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates'), '/etc/mkproject/')

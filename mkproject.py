#!/usr/bin/env python

from optparse import OptionParser
import ConfigParser
import os
import shutil
import sys

def get_file_list(directory):
    """Returns a list of the files in a directory and its subdirectories."""
    files = []
    for root, subfolders, subfiles in os.walk(directory):
        files += [os.path.join(root,file) for file in subfiles]

    return files

def mkproject(type, name, basedir=None):
    """ ``mkproject`` """
    skel = _get_projectdir(type)
    try:
        syspath = sys.path
        sys.path = [os.path.join(skel, '..')] + sys.path
        conf = __import__('%s_settings' % type, {}, {}, [], -1)
        sys.path = syspath
    except ImportError:
        conf = object()
    if not basedir:
        basedir = os.environ.get('MKPROJECT_ROOT', '.')
    if os.path.isdir(os.path.join(basedir, name)):
        raise ProjectAlreadyExists
    os.chdir(basedir)

    # populate project variables
    vars = {'name': name}
    defaults = {}
    if os.path.isfile('%s/.mkproject/mkprojectrc' % os.environ['HOME']):
        defaults = ConfigParser.RawConfigParser()
        defaults.read('%s/.mkproject/mkprojectrc' % os.environ['HOME'])
        defaults = dict(defaults.items('defaults'))
    for (var, default, desc) in getattr(conf, 'variables', ()):
        default = defaults.get(var, default)
        vars[var] = raw_input("variable: %s\n%s [%s]: " % (var, desc, default)) or default

    # run pre-installation commands
    for cmd in getattr(conf, 'pre_commands', ()):
        if callable(cmd):
            cmd(**vars)
        else:
            os.popen(cmd % vars).read()

    # copy skeleton tree to target directory
    target = os.path.join(basedir, name, getattr(conf, 'path', './') % vars)
    shutil.copytree(skel, target, symlinks=True)
    os.chdir(target)
    files = get_file_list(".")

    # replace project variables
    for (search, replace) in vars.iteritems():
        for filename in files:
            os.popen("sed -i '' 's/${%s}/%s/g' %s" % (search, replace, filename)).read()

    # run post-installation commands
    for cmd in getattr(conf, 'post_commands', ()):
        if callable(cmd):
            cmd(**vars)
        else:
            os.popen(cmd % vars).read()

    # done!
    print '%s project "%s" created at %s' % (type, name, os.path.join(basedir, name))

def _get_projectdir(type):
    basedirs = ['%s/.mkproject/' % os.environ['HOME'], '/etc/mkproject']
    for dir in basedirs:
        dir = os.path.join(dir, type)
        if os.path.isdir(dir):
            return dir
    raise UnknownProjectType

class UnknownProjectType(Exception):
    pass

class ProjectAlreadyExists(Exception):
    pass

def main():
    parser = OptionParser(usage="usage: %prog [options] <type> <name>")
    parser.add_option("-d", "--directory", dest="dir",
                  metavar="DIR", help="create project in DIR")
    (options, args) = parser.parse_args()
    if len(args) != 2:
        parser.print_help()
        sys.exit(1)
    else:
        mkproject(args[0], args[1], options.dir)

if __name__ == '__main__':
    main()


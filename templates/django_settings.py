variables = (
    ('author_name', '', "Author's name"),
    ('author_email', '', "Author's email"),
)
pre_commands = (
    'mkdir %(name)s',
    'virtualenv --no-site-packages ./%(name)s',
    'pip -E ./%(name)s install -e svn+http://code.djangoproject.com/svn/django/tags/releases/1.1#egg=django'
)
path = 'src/%(name)s'
post_commands = (
    """sed -i "" s/_SECRET_KEY_/`python -c "import random; import string; print str().join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789@#^&(-_=+)') for i in xrange(50)])"`/ settings.py""",
    'git init',
    'git add .gitignore *',
    'git commit -m "initial commit"',
)

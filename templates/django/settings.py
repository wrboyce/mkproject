import os
here = lambda path: os.path.join(os.path.realpath(__file__), path)

ADMINS = MANAGERS = (('${author_name}', '${author_email}'),)
SITE_ID = 1
SECRET_KEY = '_SECRET_KEY_'

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = here('db.sql')

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I18N = True

MEDIA_ROOT = here('static')
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

ROOT_URLCONF = '${name}.urls'
APPEND_SLASH = False

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media'
)
TEMPLATE_DIRS = (
    here('templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = '${name}_'
CACHE_MIDDLEWARE_SECONDS = 600

SEND_BROKEN_LINK_EMAILS = True
SERVER_EMAIL = '${name}@localhost'

try:
    from local_settings import *
except ImportError:
    pass

# -*- coding: utf-8 -*-
# Django settings for anar project.

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os

PROJECT_PATH = os.path.join(os.path.dirname(__file__),'..')
ROOT_PATH = PROJECT_PATH


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'anardatabase',                      # Or path to database file if using sqlite3.
        'USER': 'anar1',                      # Not used with sqlite3.
        'PASSWORD': 'anar1234',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Caracas'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-VE'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

MEDIA_ROOT = os.path.join(ROOT_PATH, 'upload')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/upload/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print "base dir path", BASE_DIR

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't^n6_$fv$4vgb^8im)t8&amp;wf$!4+f+c@+1@4-_w!mw@5j81-_t-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'AnarWeb.urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'anar.wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    PROJECT_PATH + '/AnarWeb/templates/'    
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'suit',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'AnarWeb.apps.yacimientos',
    'AnarWeb.apps.Rocas',
    #'AnarWeb.apps.DatosGenerales',
    #'AnarWeb.apps.LaManifestacion',
    #'AnarWeb.apps.Tecnicas',
    #'AnarWeb.apps.Conservacion',
    #'AnarWeb.apps.ManifestacionesAsociadas',
    #'AnarWeb.apps.Apoyos',
    #'AnarWeb.apps.Observaciones',
    #'anarapp',
    #'south',
    #'joins',
    'haystack',
	'smart_selects'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        #'ENGINE': 'xapian_backend.XapianEngine',
        #'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        'EXCLUDED_INDEXES': ['anarapp.search_indexes.BaseIndex'],
    },
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    "django.core.context_processors.request",    
)

SUIT_CONFIG = {
    # header
     'ADMIN_NAME': 'Administración de Software ANAR',
     'HEADER_DATE_FORMAT': 'l, j F Y',
     'HEADER_TIME_FORMAT': 'h:i A',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': False, # Default True

    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    """ 'MENU': (
         {'app': 'anarapp', 'icon':'icon-globe', 'label': 'Software ANAR', 'models': ('yacimiento', 'roca')},    
         {'app': 'auth', 'icon':'icon-lock', 'label': 'Usuarios', 'models': ('user', 'group')}               
     ),"""

    # misc
      'LIST_PER_PAGE': 50
}
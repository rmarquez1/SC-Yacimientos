import os
import sys


sys.path.append('/home/server/SC-Ya/')

os.environ['PYTHON_EGG_CACHE'] = '/home/server/SC-Yacimientos/AnarWeb/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
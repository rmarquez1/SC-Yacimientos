import os
import sys


sys.path.append('/home/server/SC-Yacimientos/AnarWeb/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'AnarWeb.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

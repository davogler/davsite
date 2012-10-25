import os
import sys
import site

site.addsitedir('/home/radmin/envs/dav/lib/python2.6/site-packages')

sys.path.append('/srv/www/davidalanvogler.com/')
sys.path.append('/srv/www/davidalanvogler.com/cms')



os.environ['PYTHON_EGG_CACHE'] = '/srv/www/davidalanvogler.com/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'cms.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
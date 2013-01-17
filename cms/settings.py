import os.path


DEBUG = True
TEMPLATE_DEBUG = DEBUG


#-------private settings outside of repository-----#

from settings_private import *

#-------private settings outside of repository-----#

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True


ROOT_PATH = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(ROOT_PATH, '../media')

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, '../static_local'),
)

STATIC_URL = (
	"/static/"
)

STATIC_ROOT = (
	os.path.join(ROOT_PATH, '../static')
)


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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'cms.urls'

TEMPLATE_DIRS = (
     os.path.join(ROOT_PATH, 'templates').replace('\\','/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)


#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_URL_FILEBROWSER_MEDIA =  STATIC_URL + "filebrowser/"
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(STATIC_ROOT, 'filebrowser/')
FILEBROWSER_MAX_UPLOAD_SIZE = '10485760'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Folder','Image','Document','Video','Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video','Audio'],
}

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail(60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail(60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small(140x-)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium(320x-)', 'width': 320, 'height': '', 'opts': ''},
    'work_thumbnail': {'verbose_name': 'Work Thumbnail(320x250)', 'width': 320, 'height': 250, 'opts': 'crop'},
    'big': {'verbose_name': 'Big(460x-)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large(680x-)', 'width': 680, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'work_thumbnail', 'big', 'large']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'django.contrib.markup',
    'cms.search',
    'coltrane',
    'disqus',
    'work',
    'south',
    #'debug_toolbar',
    'gunicorn',
)


#import sys

#if sys.argv[0] == 'mod_wsgi':
#    try:
#        from settings_vm import *
#    except ImportError: 
#        pass
#else:
#    try:
#        from settings_local import *
#    except ImportError:
#        pass


        
#def show_toolbar(request):
#    return True
#SHOW_TOOLBAR_CALLBACK = show_toolbar
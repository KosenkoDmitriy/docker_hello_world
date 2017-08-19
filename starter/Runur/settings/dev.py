from .base import *

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'runur',
        'USER': 'runur',
        'PASSWORD': 'P0stGr3$P45$W0rdD',
        'HOST': 'runur-server-dev.cszghbpq5kn0.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_ROOT = '/srv/starter/static'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STATICFILES_DIRS = [
#     "/srv/starter/Runur/static",
# ]
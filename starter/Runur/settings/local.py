from .base import *

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'runur',
        'USER': 'runur',
        'PASSWORD': 'ESyons55',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
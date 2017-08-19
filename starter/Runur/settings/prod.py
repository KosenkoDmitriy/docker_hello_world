from .base import *
DEBUG = False

ALLOWED_HOSTS = [ os.environ['ALLOWED_HOST'], os.environ['ALLOWED_HOST2'], os.environ['ALLOWED_HOST3'], os.environ['ALLOWED_HOST4']  ]
SECRET_KEY = os.environ['SECRET_KEY'] #'^dptwi-z99yej6$=pzz+8k30iv0+!$bn_k1(qcu#=$7@cc^4o9'

INSTALLED_APPS += (

)

DATABASES = {
    'default': {
        ## 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ENGINE': os.environ.get('PG_BACKEND', ''),
        'NAME': os.environ.get('PG_DB', ''),
        'USER': os.environ.get('PG_USER', ''),
        'PASSWORD': os.environ.get('PG_PWD', ''),
        'HOST': os.environ.get('PG_HOST', ''),
        'PORT': os.environ.get('PG_PORT', ''),
    }
}

STATIC_URL = os.environ['STATIC_URL'] #'/static/'
STATIC_ROOT = os.environ['STATIC_ROOT'] #'/srv/static-files'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STATICFILES_DIRS = [
#     "/srv/starter/Runur/static",
# ]

# Search Engine Configurations
# https://django-haystack.readthedocs.io/
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack_elasticsearch.elasticsearch2.Elasticsearch2SearchEngine',
        'URL': os.environ['HAYSTACK_URL'],
        'INDEX_NAME': os.environ['HAYSTACK_INDEX_NAME'],
    },
}

# CACHE
# REDIS CACHE FOR STREAMS
STREAM_REDIS_CONFIG = {
    'default': {
        'host': os.environ['REDIS_STREAM_HOST'],
        'port': os.environ['REDIS_STREAM_PORT'],
        'db': os.environ['REDIS_STREAM_DB'],
        'password': os.environ['REDIS_STREAM_PWD']
    },
}

DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE', '') # 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE', '') # 'storages.backends.s3boto3.S3Boto3Storage' # To allow django-admin.py collectstatic to automatically put your static files in your bucket
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN', '')

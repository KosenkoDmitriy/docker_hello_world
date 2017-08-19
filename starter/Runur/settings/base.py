"""
Django settings for Runur project.

Generated by 'django-admin startproject' using Django 1.9.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # runur app root (./starter/Runur/
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rwjkt-4wntfmzg75@z7pnu6u=3344to8wg_tz8xwg^s^dfc0_4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django Core
    #'bootstrap_admin',  #Exception
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    # 3rd party apps
    #'haystack', #django search management using ElasticSearch
    #'xadmin',
    'crispy_forms',
    'reversion', # version control for model instances https://django-reversion.readthedocs.io/en/stable/
    'polymorphic', #polymorphic models
    'rest_framework', #django-restframework
    'rest_framework_mongoengine', #django restframe mongo engine
    'rest_framework.authtoken', # django-rest-framework authtoken support
    'rest_auth', #django-rest-auth support
    'rest_framework_docs', # django-restframework document support (third party: drfdocs)

    'bootstrapform', #
    'allauth_bootstrap', #
    'allauth', #django-all-auth support
    'allauth.account', #django-all-auth support
    'rest_auth.registration', #django-RESTful authentication support
    'allauth.socialaccount', # Social Authenication
    'allauth.socialaccount.providers.facebook', # Social Authenication Facebook Support
    'allauth.socialaccount.providers.twitter', # Social Authenication Twitter Support
    'django_countries', #django-country fields support
    'location_field.apps.DefaultConfig', #django-location-fields
    'phonenumber_field',# django phone number field
    'organizations', # django-organizations
    'taggit', #django attribute tagging
    'taggit_helpers', #django attribute tagging helper
    'taggit_labels', #django attribute tagging labels
    'dddp', #django ddp intergration with meteor
    'dddp.accounts', #django ddp authentication intergration with meteor
    'qrcode', #QR Code Generation
    #'push_notifications', #django Push - Mobile Push Notification Support requires dj celery ---dependency conflicts
    'report_builder', #django Report Builder
    'corsheaders', # django-cors-headers (django Cross Origin Resource sharing header support)
    'admin_honeypot', #django Fake Adminsite for the hackers
    'changuito', # django cart support
    'localflavor', # django Local Flavor
    #'dashing', #Dashboard Utility
    'stored_messages', # django message extension for post session persistent storage
    #'django_messages',# user to user messaging ---dependency conflicts
    'django_comments_xtd',# django comments xtd
    'django_comments', # django comments
    'djangobower', # Bower Support for this site
    'schedule', # Calander
    'djgeojson', # GEOJSON support
    'mptt', # modified pre-order traversal tree
    'treenav', # Tree Navigation
    'channels', # django channels
    'django_filters', # django-filter
    'storages', # TODO django-storages for Amazon S3 (for utilizing external storage services)
    'rest_framework_raml',
    'rest_framework_swagger',

    # Runur Apps
    'API', #API Management Application
    #'JON', #Joint Operational Node Application Central Logic
    'JON.apps.JONConfig',
    'EventEngine', #django <-> meteor ddp connection
    'Search', #Search Index BUilder works with haystack
    'TaskQue',# TaskQue - Cache and Asychronous Process support
]

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Runur.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
            # Always use forward slashes, even on Windows.
            # Don't forget to use absolute paths, not relative paths.
            os.path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'treenav.context_processors.treenav_active',
            ],
        },
    },
]


WSGI_APPLICATION = 'Runur.wsgi.application'

# Authentication Backends
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Search Engine Configurations
# https://django-haystack.readthedocs.io/
HAYSTACK_CONNECTIONS = { }

# CACHE
# REDIS CACHE FOR STREAMS
STREAM_REDIS_CONFIG = { }


# Dashboards
# http://django-dashing.readthedocs.io/
DASHING = {
    'INSTALLED_WIDGETS': ('number', 'list', 'graph',),
    'PERMISSION_CLASSES':  (
        'dashing.permissions.IsAuthenticated',
    )
}

# RESTful API Framework
#http://www.django-rest-framework.org/
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,    # Standard Page Size
    'HIDE_DOCS': os.environ.get('HIDE_DRFDOCS', False),  # Default: False
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # enables simple command line authentication
        # http -a qwer:qwer1234 get http://127.0.0.1:8000/schema/ param=value
        # curl -X GET http://127.0.0.1:8000/API/users/ -H 'Authorization: <Token>'
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer', # Any other renders
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser', # Any other parsers
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

##COMMENTS + MORE
#http://django-comments-xtd.readthedocs.io/
#  Comment (level 0)
# 1: Nested up to level one:
#  Comment (level 0)
#   |-- Comment (level 1)
# 2: Nested up to level two:
#  Comment (level 0)
#   |-- Comment (level 1)
#        |-- Comment (level 2)
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 2

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Bootsrap
DJANGO_BOOTSTRAP_UI_THEME = 'bootswatch-paper'
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'starter/static')

STATICFILES_DIRS = [
    #os.path.join(os.path.dirname(BASE_DIR), 'Runur/static'), # ./starter/Runur/static
    os.path.join(BASE_DIR, 'static'), # ./starter/Runur/static
    #os.path.join(os.path.dirname(PROJECT_ROOT), 'starter/Runur/static'), # ./starter/Runur/static
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

##BOWER
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'Runur', 'components')

BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'bootstrap'
)

ORGS_SLUGFIELD = 'autoslug.fields.AutoSlugField'

GOOGLE_MAP_API_KEY = ''


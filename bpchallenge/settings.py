import os
from datetime import timedelta
import sys
import yaml

ADMINS = (('Sidon', 'sidoncd@gmail.com'),)
MANAGERS = ADMINS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'templates')

# Collect static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticbuild')

# Url in browser
STATIC_URL = '/staticbuild/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)



LOG_DIR = os.path.join(BASE_DIR, 'log')
DOC_DIR = os.path.join(BASE_DIR, 'doc')
DATA_DIR = os.path.join(BASE_DIR, 'data')

print('BASE_DIR: ', BASE_DIR)
print('STATIC_ROOT: ', STATIC_ROOT)
print('STATIC_URL: ', STATIC_URL)
print('STATIC_DIRS: ', STATICFILES_DIRS)

DEBUG = True
THUMBNAIL_DEBUG = DEBUG
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['*']


# FCONF = os.environ.get('CONFCRM')
# try:
#     with open(FCONF, 'r') as f:
#         settings = yaml.safe_load(f)
# except IOError as e:
#     print("I/O error({0}): {1}".format(e.errno, e.strerror))
#     raise
# except:
#     print('FCONF==>', FCONF)
#     print("Erro inesperado", sys.exc_info())
#     print("Erro inesperado", sys.exc_info()[0])
#     raise

# DEBUG = settings['debug']
# SECRET_KEY = settings['key']
# DATABASES = settings['db']

SECRET_KEY = 'take-a-sad-song-and-make-it-better'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SHARED_APPS = (
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.humanize',
    'django_filters',

    # Third-Party Apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'django_markup',
    'bootstrap4',

    # Project Apps
    'apps.customer',
    'apps.bpauth',
    'apps.order',
    'apps.item',
)

INSTALLED_APPS = list(SHARED_APPS)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'https://localhost:3000',
#     'http://127.0.0.1:3000',
#     'https://127.0.0.1:3000',
#     ]

CORS_ALLOW_CREDENTIALS = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

ROOT_URLCONF = 'bpchallenge.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

print('templates_PATH=>', TEMPLATE_PATH)
print('templates=>', TEMPLATES)

WSGI_APPLICATION = 'bpchallenge.wsgi.application'
AUTH_USER_MODEL = 'bpauth.User'
LOGIN_URL = '/login'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     'OPTIONS': {
         'min_length': 8,
     }},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = False

DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d/%m/%y',)
DATETIME_FORMAT = 'm/d/Y H:M:S'
DATETIME_INPUT_FORMATS = ('%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S',)
DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True


if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))
LOG_DIR = os.path.join(BASE_DIR, 'logs')


# Configurações de logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/info.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/error.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/warning.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {
            'handlers': ['mail_admins', 'console', 'file_info', 'file_error', 'file_warning'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}


DEFAULT_FROM_EMAIL = 'Sidon <sidoncd@gmail.com>'
SERVER_EMAIL = 'sidoncd@gmail.com'

SITE_HEADER = 'Brasilprev Bakend Test'
SITE_TITLE = 'Brasilprev Bakend Test'
INDEX_TITLE = 'DashBoard'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),  # TODO:
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': None,
}


# Verifica se existe um staging settings
try:
    from .staging_settings import *
except ImportError:
    pass

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend'
]

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=24),
    'JWT_ALLOW_ARGUMENT': True,
}


# # Verifica se existe um local settings
# try:
#     from .settings_local import *
# except ImportError:
#     pass

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


from datetime import timedelta
import os

ADMINS = (('Sidon', 'sidoncd@gmail.com'),)
MANAGERS = ADMINS

DEBUG = True
THUMBNAIL_DEBUG = DEBUG

SECRET_KEY = '0uarl&=3a$o1*0wk-5s@x6@d*0%r576h0&@f65+09ebtkv3jtd'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5500),  #
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5500),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# DATABASES = {
#     'default': {
#         'ENGINE': "django.db.backends.postgresql_psycopg2",
#         'NAME': 'biomed',
#         'USER': 'biomedb2b',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'SCHEMAS': 'b2b'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}


DOMAIN = 'bpchallenge'  # Usado na criação dos domínios do cliente

from bpchallenge import settings

settings.INSTALLED_APPS.append('django_extensions')

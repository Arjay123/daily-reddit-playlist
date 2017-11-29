from base_settings import *
from prod_secrets import PSQLPW

DEBUG = False

ALLOWED_HOSTS = ["ADDALLOWEDHOSTSHERE"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sample_db',
        'USER': 'sample_db_user',
        'PASSWORD': PSQLPW,
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'sample_db_test',
        }
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack/webpack-stats.json'),
    }
}
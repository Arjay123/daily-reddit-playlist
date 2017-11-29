from base_settings import *

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "localhost:8081", "localhost:80"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sample_db_stage',
        'USER': 'sample_db_stage_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'sample_db_stage_test',
        }
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack/stage-webpack-stats.json'),
    }
}
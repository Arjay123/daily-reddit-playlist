from base_settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dailyredditplaylist',
        'USER': 'dailyredditplaylistuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'dailyredditplaylisttest',
        }
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack/dev-webpack-stats.json'),
    }
}
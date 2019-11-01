from allez.settings.base import *


ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'db_allez.postgres')),
        'USER': 'allez',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


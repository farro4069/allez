from allez.settings.base import *


ALLOWED_HOSTS = ['farro4069.pythonanywhere.com']

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'db_lifecycle.sqlite3')),
    }


    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.path.join(os.path.join(BASE_DIR, 'db_allez.postgres')),
    #     'USER': 'Allez',
    #     'PASSWORD': 'allez',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
}



# try:
#     from allez.settings.local import * 
# except:
#     pass

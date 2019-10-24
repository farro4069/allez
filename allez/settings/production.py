from allez.settings.base import *


ALLOWED_HOSTS = ['farro4069.pythonanywhere.com']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'db_allez.postgres')),
    }
}





try:
    from allez.settings.local import * 
except:
    pass

from allez.settings.base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'db_hwcc.sqlite3')),
    }
}



try:
    from allez.settings.local import * 
except:
    pass

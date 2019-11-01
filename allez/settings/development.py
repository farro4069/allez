
from allez.settings.base import *


DEBUG = True

SECRET_KEY = '@4!s)gj!lc_b(!r%lw*2--h5)n*)2mjla%$o6k+p0utz!iam3b'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'db_lifecycle.sqlite3')),
    }
}


# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': 'allez',
# 		'USER': 'root',
# 		'PASSWORD': 'farro4069'
# 	}
# }



# try:
#     from allez.settings.local import * 
# except:
#     pass

from .base import *
from decouple import config


DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'literature',
        'USER': 'postgres',
        'PASSWORD': '0000',  # 여기에 PostgreSQL 비밀번호 입력
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware', )

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

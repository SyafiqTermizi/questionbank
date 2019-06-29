from .base import *  # noqa

DEBUG = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('DJANGO_MEMCACHED'),
        'TIMEOUT': 60 * 30,  # 30 minutes
    }
}

# EMAIL
EMAIL_BACKEND = os.environ.get('DJANGO_EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD')

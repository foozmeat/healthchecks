import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def bool_env(val):
    """Replaces string based environment values with Python booleans"""
    return True if os.environ.get(val, False) == 'True' else False


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = bool_env('DJANGO_DEBUG')
HOST = os.environ['DJANGO_SITE_DOMAIN']
SITE_ROOT = 'https://{0}'.format(os.environ['DJANGO_SITE_DOMAIN'])
PING_ENDPOINT = SITE_ROOT + "/ping/"
SITE_NAME = "healthchecks"

ALLOWED_HOSTS = [os.environ['DJANGO_SITE_DOMAIN']]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'djmail',
    'django_extensions',

    'hc.accounts',
    'hc.api',
    'hc.front',
    'hc.payments'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# memcached configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
        'CONN_MAX_AGE': 600
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
TIME_ZONE = 'America/Los_Angeles'

# Email
DJMAIL_REAL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
DEFAULT_FROM_EMAIL = os.environ['EMAIL_FROM']
EMAIL_USE_TLS = True

# Slack integration -- override these in local_settings
SLACK_CLIENT_ID = os.environ['SLACK_CLIENT_ID']
SLACK_CLIENT_SECRET = os.environ['SLACK_CLIENT_SECRET']

STATIC_ROOT = os.environ['STATIC_ROOT']
STATIC_URL = '/static/'

MEDIA_ROOT = os.environ['MEDIA_ROOT']
MEDIA_URL = '/media/'

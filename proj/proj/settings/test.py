from .defaults import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '192.168.26.99'
]

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'fleetCK',
        # 'NAME': 'django-test',
        'USER': 'aa',
        'PASSWORD': 'C19098)(*C19',
        'HOST': '192.168.26.127',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

# Debug Tool
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_cas_ng.middleware.CASMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         }
#     },
# }

CAS_SERVER_URL = 'http://test-cas.waipareira.com/cas/'
CAS_VERSION = '3'
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_REDIRECT_URL = '/api/admin/'

LOGOUT_REDIRECT_URL = '/api/admin/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 14400  # (4h)

# email_notification Settings
EMAIL_CARRIER = {
    'name': 'celery',
    'CELERY_API_KEY': '$s0xzks2iy*wo*3y',
    'CELERY_EMAIL_API_ENDPOINT': 'http://test-queue.waicloud.co/email/',
}
DEFAULT_FROM_EMAIL = 'no-reply@waiwhanau.com'

TEMPLATE_CHOICES = [
    # notify
    ('Vehicle Booked', 'Vehicle Booked'),
    ('Vehicle Returned', 'Vehicle Returned'),
]
#

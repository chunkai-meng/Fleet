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

CAS_SERVER_URL = 'http://test-cas.waipareira.com/cas/'
CAS_VERSION = '3'
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_REDIRECT_URL = '/api/admin/'

LOGOUT_REDIRECT_URL = '/api/admin/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 14400  # (4h)

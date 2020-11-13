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
# CAS_SERVER_URL = 'http://0.0.0.0:8003/cas/'
# DOMAIN = 'http://127.0.0.1:8000'
# CAS_REDIRECT_URL = '/api/admin/'
# SIMPLE_HISTORY_REVERT_DISABLED = True

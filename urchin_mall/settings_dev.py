import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "urchin_mall",
        "USER": "sqljohn",
        "PASSWORD": "123",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        # "OPTIONS": {"charset": "utf8mb4"},
        # "TEST": {"CHARSET": "utf8mb4"},
        # "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_URL = "http://192.168.2.125:8000"

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.2.125']

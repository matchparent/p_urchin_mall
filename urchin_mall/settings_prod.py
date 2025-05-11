import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "urchin_mall",
        "USER": "admin",
        "PASSWORD": "asdf1234",
        "HOST": "db-urchin-mall.ckxk6o6mm5y3.us-east-1.rds.amazonaws.com",
        "PORT": "3306",
        # "OPTIONS": {"charset": "utf8mb4"},
        # "TEST": {"CHARSET": "utf8mb4"},
        # "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_URL = "http://3.95.181.121:8000"

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['3.95.181.121']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.2.125']

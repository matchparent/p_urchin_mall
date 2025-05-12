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

IMAGE_URL = BASE_URL + "/static/product_images/"

ALIPAY_APPID = "2021000148636567"

# async receiving url, post
APP_NOTIFY_URL = BASE_URL + "/alipay/return"
# sync receiving url, e.i. page after payment settled, get
APP_RETURN_URL = BASE_URL + "/alipay/return"

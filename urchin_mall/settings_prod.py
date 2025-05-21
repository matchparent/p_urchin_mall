import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "railway",
        "USER": "root",
        "PASSWORD": "hEKMpRbVgZXrxSllGxORlauPzJXRawOD",
        "HOST": "gondola.proxy.rlwy.net",
        "PORT": "37109",
        # "OPTIONS": {"charset": "utf8mb4"},
        # "TEST": {"CHARSET": "utf8mb4"},
        # "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# BASE_URL = "http://3.95.181.121"
BASE_URL = "https://api.urchin.website"

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['3.95.181.121']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.2.125']


IMAGE_URL = BASE_URL + "/static/product_images/"

ALIPAY_APPID = "2021000148636567"

# async receiving url, post
APP_NOTIFY_URL = BASE_URL + "/alipay/return"
# sync receiving url, e.i. page after payment settled, get
APP_RETURN_URL = BASE_URL + "/alipay/return"

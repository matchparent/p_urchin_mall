import datetime

import jwt
from rest_framework.authentication import BaseAuthentication

from urchin_mall.settings import SECRET_KEY


def generate_token(payload):
    headers = {
        "alg": "HS256", "typ": "JWT"
    }
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(hours=24)

    token = jwt.encode(payload, SECRET_KEY, headers=headers, algorithm="HS256")
    return token


def get_payload(token):
    rst = {"status": 505, "data": ""}
    try:
        rst["data"] = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        rst["status"] = 200
    except jwt.exceptions.DecodeError as e:
        rst["data"] = "token decode failed"
    except jwt.exceptions.ExpiredSignatureError as e:
        rst["data"] = "token has expired"
    except jwt.exceptions.InvalidTokenError as e:
        rst["data"] = "token is invalid"
    return rst


# get token from url, e.g. /?token=asdfqwer
class JwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get("token")
        payload = get_payload(token)
        return payload, token


class JwtHeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # when send request,add token = ... in headers. Here, auto add http_ and upper cased, renamed as HTTP_TOKEN
        # token = request.META.get("HTTP_TOKEN")    # this is for postman
        token = request.META.get("HTTP_AUTHORIZATION")  # this is for chrome
        payload = get_payload(token)
        return payload, token

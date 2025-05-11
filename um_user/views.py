from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from um_user.models import UserSerializer, User
from utils.Token import generate_token
from utils.UmResponse import UmResponse
from utils.StringUtil import getmd5


# Create your views here.
class UserAPIView(APIView):
    # def post(self, request):
    #     request.data['password'] = getmd5(request.data.get('password'))
    #     # anti-serialize a json to an object
    #     userserializer = UserSerializer(data=request.data)
    #     userserializer.is_valid(raise_exception=True)
    #     data = User.objects.create(**userserializer.data)
    #
    #     # serialize and return json to front-end
    #     user = UserSerializer(instance=data)
    #     return UmResponse.jrGen(UmResponse.status_200, user.data)

    # register
    # md5 transfered to serializer.create()
    def post(self, request):
        # anti-serialize a json to an object
        try:
            userserializer = UserSerializer(data=request.data)
            userserializer.is_valid(raise_exception=True)
            data = userserializer.save()
            # serialize and return json to front-end
            user = UserSerializer(instance=data)
            return UmResponse.jr_gen(UmResponse.status_200, user.data)
        except Exception as e:
            # print(e)::: {'email': [ErrorDetail(string='account already created', code='unique')]}
            msg = str(e.detail['email'][0])
            return UmResponse.jr_gen(500, msg)

    # get user information
    def get(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        try:
            data = User.objects.get(email=email)
            ser_data = UserSerializer(instance=data)
            return UmResponse.jr_gen(UmResponse.status_200, ser_data.data)
        except Exception as e:
            return UmResponse.jr_gen(500, str(e))

    def put(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        try:
            User.objects.filter(email=email).update(**request.data)
            return UmResponse.jr_gen(200, "update success.")
        except Exception as e:
            return UmResponse.jr_gen(500, str(e))


class LoginGAV(generics.GenericAPIView):

    def post(self, request):
        un = request.data.get('username')
        ps = request.data.get('password')

        try:
            data = User.objects.get(email=un, password=getmd5(ps))
        except Exception as e:
            data = None

        if not data:
            return UmResponse.jr_gen(500, "username or password error")
        else:
            # userserializer = UserSerializer(instance=data, many=False)
            token_info = {
                "email": un
            }
            token = generate_token(token_info)
            rst = {"token": token, "username": un}
            return UmResponse.jr_gen(200, rst)

    def get(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        else:
            return UmResponse.jr_gen(200, "status legal")

    def put(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        op = request.data['op']
        np = request.data['np']

        user = User.objects.filter(email=email, password=getmd5(op))
        if user.first():
            user.update(password=getmd5(np))
            return UmResponse.jr_gen(200, "Password updated")
        else:
            return UmResponse.jr_gen(500, "Input username or password error")

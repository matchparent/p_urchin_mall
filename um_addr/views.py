from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from um_addr.models import UserAddress, UserAddressSerializer
from utils.Token import JwtAuthentication, JwtHeaderAuthentication
from utils.UmResponse import UmResponse


# Create your views here.
class AddressGAV(GenericAPIView, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = UserAddress.objects
    serializer_class = UserAddressSerializer
    authentication_classes = [JwtHeaderAuthentication]

    def get(self, request):
        return UmResponse.jr_gen(200, "test success")

    def post(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        request.data["email"] = email
        request.data["default"] = 1 if request.data["default"] else 0
        if request.data["default"] == 1:
            self.get_queryset().filter(email=email).update(default=0)
        return UmResponse.jr_gen(200, self.create(request).data)
        # return self.create(request)

    # def get(self, request, pk):
    #     if request.user.get("status") == 505:
    #         return UmResponse.jr_gen(507, request.user.get("data"))
    #     return self.retrieve(request, pk)

    def put(self, request, pk):
        request.data["default"] = 1 if request.data["default"] else 0
        return UmResponse.jr_gen(200, self.update(request, pk).data)
        # return self.update(request, pk)

    def delete(self, request, pk):
        return UmResponse.jr_gen(200, self.destroy(request, pk).data)
        # return self.destroy(request, pk)


# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjRAcXEuY29tIiwiZXhwIjoxNzQ0NDg5MDE0fQ.VmKS1_Yz7Jw3ekYwMAWe-spVdNnH5HXWrDGq9bTf1l0
class AddressListGAV(GenericAPIView, ListModelMixin):
    queryset = UserAddress.objects
    serializer_class = UserAddressSerializer
    # JwtAuthentication run before get/post etc. methods. authentication_classes, field from APIView
    authentication_classes = [JwtHeaderAuthentication]

    # def get_queryset(self):
    #     email = self.request.user.get("data", {}).get("email")
    #     if not email:
    #         return UserAddress.objects.none()  # 或者 raise PermissionDenied()
    #     return UserAddress.objects.filter(email=email)

    # def get(self, request):
    # JwtAuthentication.authenticate, returns payload, token
    # user is payload, auth is token
    # print(request.user)
    # print(request.auth)
    # return self.list(request)

    def get(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        queryset = self.get_queryset().filter(email=email).order_by("-default")
        return UmResponse.jr_gen(200, self.get_serializer(instance=queryset, many=True).data)

    def put(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        self.get_queryset().filter(email=email).update(default=0)
        self.get_queryset().filter(id=request.data['id']).update(default=1)
        return UmResponse.jr_gen(200, "address default updated")

from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from um_cart.models import ShoppingCart, CartSerializer, CartSerializer2
from utils.UmResponse import UmResponse


# Create your views here.
class CartAPIView(APIView):
    # def post(self, request):
    #     # mail = request.data['mail']
    #     email = request.data.get('email')  # using ['mail'], if can't access to the field, error thrown
    #     nums = request.data.get('nums')
    #     sku_id = request.data.get('sku_id')
    #     is_delete = request.data.get('is_delete')
    #     data = ShoppingCart.objects.filter(email=email, is_delete=0, sku_id=sku_id)
    #     if data.exists():
    #         if is_delete == 0:
    #             request.data['nums'] = data.get(email=email, is_delete=0, sku_id=sku_id).nums + nums
    #         else:
    #             request.data['nums'] = data.get(email=email, is_delete=0, sku_id=sku_id).nums
    #         # anti-serialize
    #         cart_ser = CartSerializer(data=request.data)
    #         cart_ser.is_valid(raise_exception=True)
    #         ShoppingCart.objects.filter(email=email, is_delete=0, sku_id=sku_id).update(**cart_ser.data)
    #
    #         return UmResponse.gen(UmResponse.status_200, "update success." if is_delete == 0 else "delete success.")
    #
    #     else:
    #         cart_ser = CartSerializer(data=request.data)
    #         cart_ser.is_valid(
    #             raise_exception=True)  # verify whether field type match or not, example rule in CartSerializer
    #         ShoppingCart.objects.create(**cart_ser.data)
    #         # return UmResponse.gen(UmResponse.status_200, "insert success.")
    #         return JsonResponse({"status": 200, "data": "insert success."})

    def post(self, request):
        # request.user: {'status': 200, 'data': {'email': '4@qq.com', 'exp': 1745396949}}
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        request.data['email'] = email
        nums = request.data.get('nums')
        append = request.data.pop('append', False)
        sku_id = request.data.get('sku_id')
        is_delete = request.data.get('is_delete', 0)
        data = ShoppingCart.objects.filter(email=email, is_delete=0, sku_id=sku_id)
        if data.exists():
            if append:
                nums = data.get(email=email, is_delete=0, sku_id=sku_id).nums + nums
            else:
                nums = nums

            if is_delete == 0:
                ShoppingCart.objects.filter(email=email, is_delete=0, sku_id=sku_id).update(nums=nums)
            else:
                ShoppingCart.objects.filter(email=email, sku_id=sku_id).update(is_delete=1)
            return UmResponse.gen(UmResponse.status_200, "update success." if is_delete == 0 else "delete success.")
        else:
            # insert = {
            #     "email": email,
            #     "nums": nums,
            #     "sku_id": sku_id,
            #     "is_delete": 0,
            # }
            # cart_ser = CartSerializer2(data=insert)
            cart_ser = CartSerializer2(data=request.data)
            cart_ser.is_valid(
                raise_exception=True)  # verify whether field type match or not, example rule in CartSerializer
            ShoppingCart.objects.create(**cart_ser.data)
            # return UmResponse.gen(UmResponse.status_200, "insert success.")
        return JsonResponse({"status": 200, "data": "insert success."})

    # def get(self, request):
    #     seralizing plural rows of data, many=True
    #     safe=False: allow types such as jsonarray
    #     else:
    #         return JsonResponse(
    #             {"status": 200,
    #              "data": CartSerializer(
    #                  instance=ShoppingCart.objects.filter(email=request.GET.get('email'), is_delete=0),
    #                  many=True).data}, safe=False)Ï

    def get(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        cart = ShoppingCart.objects.filter(email=email, is_delete=0).all()
        return UmResponse.gen(UmResponse.status_200, CartSerializer(cart, many=True).data)

    def delete(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        # ShoppingCart.objects.filter(request.data).update(is_delete=1)
        # sku_id__in, whether skuid is in [], which is request.data
        ShoppingCart.objects.filter(email=email, sku_id__in=request.data, is_delete=0).update(is_delete=1)
        return UmResponse.gen(UmResponse.status_200, "delete success.")


class CartCountAPIView(APIView):
    def get(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        cart = ShoppingCart.objects.filter(email=email, is_delete=0).aggregate(nums=Sum('nums'))
        return UmResponse.gen(UmResponse.status_200, cart)
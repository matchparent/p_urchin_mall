from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from um_cart.models import ShoppingCart
from um_order.models import OrderGoods, OrderGoodsSerializer, Order, OrderSerializer, OrderDtailSerializer
from utils.UmResponse import UmResponse
import time


# Create your views here.
class OrderGoodsGenericApiView(GenericAPIView):
    queryset = OrderGoods.objects
    serializer_class = OrderGoodsSerializer

    def post(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return UmResponse.jr_gen(UmResponse.status_200, ser.data)

    # def get(self, request):
    # query all data
    # return UmResponse.jr_gen(UmResponse.status_200, self.get_serializer(instance=self.get_queryset(), many=True).data)

    lookup_field = "trade_no"

    def get(self, request, trade_no):
        # get_object deal return of just one, if many, even if many=True, will be problem
        # get_object() find field name from lookup_field, value is trade_no
        # if want many plural results,  e.g. instance = self.get_queryset().filter(...).first
        return UmResponse.jr_gen(UmResponse.status_200,
                                 self.get_serializer(instance=self.get_object(), many=False).data)


class OrderGenericApiView(GenericAPIView):
    queryset = Order.objects
    serializer_class = OrderSerializer

    def post(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        trade_no = int(time.time() * 1000)

        data_trade = request.data["trade"]
        data_goods = request.data["goods"]
        data_trade["trade_no"] = trade_no
        data_trade["email"] = email
        data_trade["pay_status"] = 0
        data_trade["is_delete"] = 0

        serializer = self.get_serializer(data=data_trade)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        item = {}
        for goods in data_goods:
            item["trade_no"] = trade_no
            item["sku_id"] = goods["sku_id"]
            item["goods_num"] = goods["nums"]
            OrderGoods.objects.create(**item)
            ShoppingCart.objects.filter(email=email, sku_id=item["sku_id"]).update(is_delete=1)
        return UmResponse.jr_gen(UmResponse.status_200, {"trade_no": trade_no})

    def get(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        pay_status = request.GET.get("pay_status")

        if not pay_status or pay_status == "-1":
            dbrst = Order.objects.filter(email=email, is_delete=0).all().order_by("-create_time")
        else:
            dbrst = Order.objects.filter(email=email, is_delete=0, pay_status=pay_status).all().order_by("-create_time")

        ods = OrderDtailSerializer(instance=dbrst, many=True).data
        return UmResponse.jr_gen(UmResponse.status_200, ods)

    def delete(self, request):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        Order.objects.filter(email=email, trade_no=request.data['trade_no'], is_delete=0).update(is_delete=1)
        return UmResponse.jr_gen(200, "delete success.")


class OrderDetailGAV(GenericAPIView):
    queryset = Order.objects
    serializer_class = OrderDtailSerializer

    lookup_field = "trade_no"

    def get(self, request, trade_no):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]

        return UmResponse.jr_gen(UmResponse.status_200, self.get_serializer(instance=self.get_object(), many=False).data)

    def put(self, request, trade_no):
        if request.user.get("status") == 505:
            return UmResponse.jr_gen(507, request.user.get("data"))
        email = request.user["data"]["email"]
        self.get_queryset().filter(email=email, trade_no=trade_no).update(**request.data)
        return UmResponse.jr_gen(200, "pay success.")

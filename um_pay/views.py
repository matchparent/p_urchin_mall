from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from um_order.models import Order
from um_pay.alipay import AliPay


# pip install pycryptodome

class PayAPIView(APIView):

    def post(self, request):
        alipay = AliPay()

        url = alipay.direct_pay(
            **request.data
        )

        re_url = alipay.gateway + "?{data}".format(data=url)
        return JsonResponse({"status": 200, "data": re_url})


class PayReturnAPIView(APIView):
    def get(self, request):
        dic_rd = {}
        for k, v in request.GET.items():
            dic_rd[k] = v
        sign = dic_rd.pop("sign", None)
        alipay = AliPay()
        if alipay.verify(dic_rd, sign):
            Order.objects.filter(trade_no=dic_rd["out_trade_no"]).update(pay_status=2, ali_trade_no=dic_rd["trade_no"],
                                                                         pay_time=datetime.now())
            return redirect("http://192.168.2.125:8080/profile/?activeIndex=3")
        else:
            return JsonResponse({"status": 500, "data": "fail"})

    def post(self, request):
        dic_rd = {}
        for k, v in request.POST.items():
            dic_rd[k] = v
        sign = dic_rd.pop("sign", None)
        alipay = AliPay()
        if alipay.verify(dic_rd, sign):
            Order.objects.filter(trade_no=dic_rd["out_trade_no"]).update(pay_status=2, ali_trade_no=dic_rd["trade_no"],
                                                                         pay_time=datetime.now())
            return JsonResponse({"status": 200, "data": "success"})
        else:
            return JsonResponse({"status": 500, "data": "fail"})

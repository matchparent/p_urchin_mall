from django.urls import path, re_path
from .views import OrderGoodsGenericApiView, OrderGenericApiView, OrderDetailGAV

urlpatterns = [
    path("", OrderGenericApiView.as_view()),
    path("goods/", OrderGoodsGenericApiView.as_view()),
    re_path("detail/(?P<trade_no>.*)", OrderDetailGAV.as_view()),
    re_path("goods/(?P<trade_no>.*)", OrderGoodsGenericApiView.as_view()),

]

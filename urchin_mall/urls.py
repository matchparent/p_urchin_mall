"""
URL configuration for urchin_mall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demoo.views import splurge
from um_menu.views import MainMenuView, SubMenuView
from um_pay.views import PayAPIView, PayReturnAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("splurgee", splurge),
    path("main_menu", MainMenuView.as_view()),
    path("sub_menu", SubMenuView.as_view()),
    path("commodity/", include("um_commodity.urls")),
    path("cart/", include("um_cart.urls")),
    path("user/", include("um_user.urls")),
    path("order/", include("um_order.urls")),
    path("addr/", include("um_addr.urls")),
    path("comment/", include("um_comment.urls")),
    path("pay", PayAPIView.as_view()),
    path("alipay/return", PayReturnAPIView.as_view()),
]

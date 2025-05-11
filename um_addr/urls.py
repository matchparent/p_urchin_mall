from django.urls import path, re_path
from .views import AddressGAV, AddressListGAV

urlpatterns = [
    path("", AddressGAV.as_view()),
    path("list", AddressListGAV.as_view()),
    re_path("(?P<pk>.*)", AddressGAV.as_view()),
]

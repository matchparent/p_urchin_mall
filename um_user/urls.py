from django.urls import path
from .views import UserAPIView,LoginGAV

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("login/", LoginGAV.as_view()),
]

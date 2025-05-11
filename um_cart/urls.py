from django.urls import path
from .views import CartAPIView, CartCountAPIView

urlpatterns = [
    path("", CartAPIView.as_view()),
    path("count", CartCountAPIView.as_view()),
]

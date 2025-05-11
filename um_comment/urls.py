from django.urls import path, re_path
from .views import CommentGAV

urlpatterns = [
    path("", CommentGAV.as_view({
        "get": "listt",
        "post": "createe"
    })),
    re_path("(?P<pk>.*)", CommentGAV.as_view({
        "get": "singlee",
        "post": "editt",
        "delete": "delette"
    })),
]

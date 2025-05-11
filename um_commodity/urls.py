from django.urls import path
from .views import CommodityCategoryAPIView, CommodityDetailAPIView, CommodityFlashSaleAPIView, CommoditySearchAPIView

urlpatterns = [
    path("flash", CommodityFlashSaleAPIView.as_view()),
    path("category/<int:cateid>/<int:page>", CommodityCategoryAPIView.as_view()),
    path("<str:sku_id>", CommodityDetailAPIView.as_view()),
    path("search/<str:keyword>/<int:page>/<int:order_by>", CommoditySearchAPIView.as_view()),

]

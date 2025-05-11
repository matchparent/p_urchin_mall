# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers

from um_commodity.models import GoodsSerializer, Goods
from urchin_mall.settings import IMAGE_URL


class ShoppingCart(models.Model):
    sku_id = models.CharField(max_length=255)
    nums = models.IntegerField()
    is_delete = models.IntegerField()
    email = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart'

class CartSerializer2(serializers.Serializer):
    sku_id = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    nums = serializers.IntegerField()
    is_delete = serializers.IntegerField()

class CartSerializer(serializers.Serializer):
    sku_id = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    nums = serializers.IntegerField()
    is_delete = serializers.IntegerField()

    commodity = serializers.SerializerMethodField()

    def get_commodity(self, obj):
        return GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).first()).data
        # return GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).all(), many=True).data

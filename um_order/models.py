# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers

from um_addr.models import UserAddressSerializer, UserAddress
from um_commodity.models import Goods
from urchin_mall.settings import IMAGE_URL


class Order(models.Model):
    trade_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    pay_status = models.CharField(max_length=155, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    ali_trade_no = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    # update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderGoods(models.Model):
    trade_no = models.CharField(max_length=255, blank=True, null=True)
    sku_id = models.CharField(max_length=255, blank=True, null=True)
    goods_num = models.IntegerField(blank=True, null=True)

    # create_time = models.DateTimeField(blank=True, null=True)     # annotate is to avoid overwrite of auto-generated create_time

    class Meta:
        managed = False
        db_table = 'order_goods'


class OrderGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGoods
        fields = '__all__'


class OrderDtailSerializer(serializers.Serializer):
    trade_no = serializers.CharField()
    email = serializers.CharField()
    order_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    address_id = serializers.IntegerField()
    pay_status = serializers.CharField()
    pay_time = serializers.DateTimeField()
    ali_trade_no = serializers.CharField()
    is_delete = serializers.IntegerField()
    create_time = serializers.DateTimeField(read_only=True)

    order_goods = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    def get_receiver(self, obj):
        if not obj.address_id:
            return ''
        else:
            addr = UserAddress.objects.filter(id=obj.address_id).first()
            return addr.signer_name

    def get_order_goods(self, obj):
        ogs = OrderGoodsSerializer(OrderGoods.objects.filter(trade_no=obj.trade_no).all(), many=True).data
        for i in ogs:
            item = Goods.objects.get(sku_id=i['sku_id'])
            i['p_price'] = item.p_price
            i['image'] = IMAGE_URL + item.image
            i['name'] = item.name
            i['shop_name'] = item.shop_name
            if not i['goods_num']:
                i['goods_num'] = 1
        return ogs

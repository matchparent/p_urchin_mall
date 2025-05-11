# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import json

from django.db import models
from django.forms.models import model_to_dict

from urchin_mall.settings import IMAGE_URL
from utils.Encoders import DecimalEncoder

from rest_framework import serializers


class Goods(models.Model):
    type_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sku_id = models.CharField(max_length=255, blank=True, null=True)
    target_url = models.CharField(max_length=255, blank=True, null=True)
    jd_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    spu_id = models.CharField(max_length=255, blank=True, null=True)
    mk_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vender_id = models.IntegerField(blank=True, null=True)
    find = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     try:
    #         return json.dumps(model_to_dict(self), ensure_ascii=False)
    #     except Exception as e:
    #         return f"<SubMenu object (error in __str__): {e}>"

    def __str__(self):
        return json.dumps({
            'type_id': self.type_id,
            'name': self.name,
            'sku_id': self.sku_id,
            'target_url': self.target_url,
            'jd_price': self.jd_price,
            'p_price': self.p_price,
            'image': IMAGE_URL + self.image,
            'shop_name': self.shop_name,
            'shop_id': self.shop_id,
            'spu_id': self.spu_id,
            'mk_price': self.mk_price,
            'vender_id': self.vender_id,
            'find': self.find,
            'create_time': self.create_time,

        }, cls=DecimalEncoder, ensure_ascii=False)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsSerializer(serializers.ModelSerializer):
    # fields need to be taken care of
    image = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_image(self, obj):
        return IMAGE_URL + obj.image

    class Meta:
        model = Goods
        fields = '__all__'

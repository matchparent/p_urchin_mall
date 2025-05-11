# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime

from django.db import models
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from utils.StringUtil import getmd5


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserSerializer(serializers.ModelSerializer):
    # unique email check
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, validators=[
        UniqueValidator(queryset=User.objects.all(), message="account already created")])

    # here to stop returning password when get
    password = serializers.CharField(write_only=True)

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    birthday = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data):
        validated_data['password'] = getmd5(validated_data['password'])
        validated_data['create_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = '__all__'

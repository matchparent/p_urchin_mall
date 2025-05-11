# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import json

from django.db import models


class MainMenu(models.Model):
    main_menu_id = models.IntegerField()
    main_menu_name = models.CharField(max_length=255)
    main_menu_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return json.dumps({
            'main_menu_id': self.main_menu_id,
            "main_menu_name": self.main_menu_name,
            # "main_menu_url": self.main_menu_url
        }, ensure_ascii=False)

    class Meta:
        managed = False
        db_table = 'main_menu'


class SubMenu(models.Model):
    main_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_type = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_name = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return json.dumps({
            'main_menu_id': self.main_menu_id,
            "sub_menu_id": self.sub_menu_id,
            "sub_menu_type": self.sub_menu_type,
            "sub_menu_name": self.sub_menu_name,
            "sub_menu_url": self.sub_menu_url,
        }, ensure_ascii=False)

    class Meta:
        managed = False
        db_table = 'sub_menu'

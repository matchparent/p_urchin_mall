from django.db import models


# generate table in db from django:
# 1. create migrations folder and content:  python manage.py makemigrations demoo
# 2. create table:                          python manage.py migrate

# Create your models here.
class TabDemo(models.Model):
    tdid = models.AutoField(primary_key=True, auto_created=True, null=False, unique=True)
    tdstr = models.CharField(max_length=255, null=False)
    tdint = models.IntegerField(null=False)
    tdboo = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tab_demo'  # table name

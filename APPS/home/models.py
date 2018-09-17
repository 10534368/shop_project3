from django.db import models

# Create your models here.
class Navigation(models.Model):
    nav_id = models.AutoField(primary_key=True)
    nav_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'navigation'

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=200)
    order = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'

class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'

class SubMenu(models.Model):
    sub_menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cate = models.ForeignKey('Category', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_menu'

class SubMenu2(models.Model):
    sub_menu2_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sub_menu = models.ForeignKey('SubMenu', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_menu2'

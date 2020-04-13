from django.db import models


class ShopInfo(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_desc = models.CharField(max_length=255, blank=True)
    shop_address = models.CharField(max_length=255, blank=True)
    shop_email = models.CharField(max_length=255, blank=True)
    shop_password = models.CharField(max_length=255, blank=True)
    shop_phone_1 = models.CharField(max_length=255, blank=True)
    shop_phone_2 = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)
    shop_token = models.CharField(max_length=255, blank=True)


class UsrInfo(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_email = models.EmailField(max_length=255, blank=True)
    usr_f_name = models.CharField(max_length=255, blank=True)
    usr_l_name = models.CharField(max_length=255, blank=True)
    usr_phone = models.CharField(max_length=255, blank=True)
    usr_address = models.CharField(max_length=255, blank=True)
    usr_password = models.CharField(max_length=255, blank=True)
    shop_id = models.ForeignKey(ShopInfo, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1)
    usr_token = models.CharField(max_length=255, blank=True)


class CategoryTable(models.Model):
    category_id = models.AutoField(primary_key=True)
    shop_id = models.ForeignKey(ShopInfo, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)


class SubCategoryTable(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(CategoryTable, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)


class ItemTypes(models.Model):
    item_types_id = models.AutoField(primary_key=True)
    sub_category_id = models.ForeignKey(SubCategoryTable, on_delete=models.CASCADE)
    item_types = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)


class ItemInfo(models.Model):
    item_info_id = models.AutoField(primary_key=True)
    item_types_id = models.ForeignKey(ItemTypes, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, blank=True)
    item_unit_price = models.CharField(max_length=255, blank=True)
    item_minimum_qty = models.CharField(max_length=255, blank=True)
    item_unit = models.CharField(max_length=255, blank=True)
    item_image = models.CharField(max_length=255, blank=True)
    item_info_1 = models.CharField(max_length=255, blank=True)
    item_info_2 = models.CharField(max_length=255, blank=True)
    item_info_3 = models.CharField(max_length=255, blank=True)
    item_info_4 = models.CharField(max_length=255, blank=True)
    item_info_5 = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)

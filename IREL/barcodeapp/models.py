from __future__ import unicode_literals

from django.db import models

class Godown(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Rack(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Shelf(models.Model):

    shelf_name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return self.shelf_name


class Product(models.Model):
    product_code = models.CharField(max_length=15,null=True)
    name = models.CharField(max_length=255,null=True)
    value=models.IntegerField(null=True)
    barcode=models.CharField(max_length=15,null=True)
    unity_of_measurement = models.CharField(max_length=255, default='NOS')
    lrd = models.DateField(blank=True, null=True)
    lid = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(null=True)

    def __str__(self):
        return str(self.product_code)


# class Productrequisition(models.Model):
#     product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product')
#     purchaserequisition = models.ForeignKey('Purchaserequisition', models.DO_NOTHING, db_column='purchaserequisition')


# class Purchaserequisition(models.Model):
#     department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
#     capital_or_revenue = models.CharField(max_length=255)
#     indent_no = models.IntegerField(blank=True, null=True)
#     indentor_name = models.CharField(max_length=255)
#     indentor_designation = models.CharField(max_length=255)
#     purpose_of_procurement = models.CharField(max_length=255)
#     nature_of_indent = models.CharField(max_length=255)
#     section_code = models.IntegerField(blank=True, null=True)
#     count = models.IntegerField()
#     fullfilled_or_not = models.IntegerField()
#     fullfilled_date = models.DateTimeField(blank=True, null=True)

class Inspection(models.Model):
    purchase_order_no=models.CharField(max_length=150)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_time=models.DateTimeField()
    gate_pass_no=models.CharField(max_length=150)


class Exit(models.Model):
    product_requisition_no=models.CharField(max_length=150)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product')
    issued_or_not = models.CharField(max_length=15)
    issued_to = models.ForeignKey(Department, models.DO_NOTHING, db_column='issued_to', blank=True, null=True)
    issued_date = models.DateTimeField()
    issuer_email_id=models.CharField(max_length=150)


class Stock(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    existing_quantuty=models.IntegerField()
    storage_place=models.ForeignKey(Shelf,on_delete=models.CASCADE)

class Shelfsticker(models.Model):
    godown=models.ForeignKey(Godown,on_delete=models.CASCADE)
    rack=models.ForeignKey(Rack,on_delete=models.CASCADE)
    shelf=models.CharField(max_length=150)


    def __str__(self):
        return (str(self.godown)+str(self.rack)+str(self.shelf))

class Productsticker(models.Model):
    product_code=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_code)
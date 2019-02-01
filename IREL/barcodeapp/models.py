from __future__ import unicode_literals

from django.db import models
import datetime
import calendar
import django.utils.timezone

def return_date_time():
    now = datetime.date.today()
    return now + datetime.timedelta(days=700)

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Godown(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Godown, self).save(*args, **kwargs)


class Rack(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Rack, self).save(*args, **kwargs)


class Shelf(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Shelf, self).save(*args, **kwargs)


class ShelfSticker(models.Model):
    godown=models.ForeignKey(Godown,on_delete=models.CASCADE)
    rack=models.ForeignKey(Rack,on_delete=models.CASCADE)
    shelf=models.ForeignKey(Shelf,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id).zfill(6)

    class Meta:
        unique_together = ('godown', 'rack', 'shelf')


class PurchaseOrder(models.Model):
    purchase_order_no=models.CharField(max_length=150)

    def __str__(self):
        return self.purchase_order_no


class Product(models.Model):
    PADS= 'PADS'
    NOS = 'NOS'
    DOZEN = 'DOZEN'
    SET='SET'
    KGS='KGS'
    LEN='LEN'
    LIT='LIT'
    BOT='BOT'
    SQM='SQM'
    PKT='PKT'
    MTR='MTR'
    BUN='BUN'
    product_choises = (
        (NOS, 'NOS'), (DOZEN, 'DZ'), (PADS, 'PD'),(SET,'SET'),(LEN,'LEN'),(KGS,'KGS'),(LIT,'LIT'),
        (BOT,'BOT'),(SQM,'SQM'),(PKT,'PKT'),(MTR,"MTR"),(BUN,'BUN')
    )
    product_code = models.CharField(max_length=15,null=True)
    name = models.CharField(max_length=255,null=True)
    value=models.FloatField(default=0.00,null=True,blank=True)
    barcode=models.CharField(max_length=15,null=True,blank=True)
    unity_of_measurement = models.CharField(max_length=255, choices=product_choises)
    last_received_date = models.DateField(default=datetime.date.today,blank=True,null=True)
    last_issued_date = models.DateField(default=return_date_time(),blank=True,null=True)
    quantity=models.IntegerField()
    godown=models.CharField(max_length=50)
    rack=models.CharField(max_length=50)
    shelf=models.CharField(max_length=50)


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
    product=models.ManyToManyField(Product)
    quantity=models.IntegerField()
    date_time=models.DateTimeField(default=django.utils.timezone.now)
    gate_pass_no=models.CharField(max_length=150)

    def __str__(self):
        return self.purchase_order_no


class Exit(models.Model):
    product_requisition_no=models.CharField(max_length=150)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity_to_exit=models.IntegerField()
    issued_or_not = models.CharField(max_length=15)
    issued_to = models.ForeignKey(Department, models.DO_NOTHING, db_column='issued_to', blank=True, null=True)
    issued_date = models.DateField(default=datetime.date.today)
    issuer_email_id=models.CharField(max_length=150)

    def __str__(self):
        return self.product_requisition_no

class Stock(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    existing_quantuty=models.IntegerField()
    storage_place=models.ForeignKey(Shelf,on_delete=models.CASCADE)


class ProductSticker(models.Model):
    product_code=models.ManyToManyField(Product)

    def __str__(self):
        return str(self.product_code)

class ProductInscan(models.Model):
     product = models.CharField(max_length=150)
     date_time = models.DateTimeField(default=django.utils.timezone.now)
     status = models.IntegerField(blank=True, null=True)

# Generated by Django 2.1.3 on 2018-11-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0007_auto_20181120_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lid',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lrd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='unity_of_measurement',
            field=models.CharField(default='NOS', max_length=255),
        ),
    ]

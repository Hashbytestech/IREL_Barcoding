# Generated by Django 2.1.3 on 2018-11-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0006_auto_20181120_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelfsticker',
            name='barcode',
        ),
        migrations.AddField(
            model_name='shelf',
            name='barcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-17 12:17

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0006_auto_20181217_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exit',
            name='product',
        ),
        migrations.AddField(
            model_name='exit',
            name='product',
            field=models.ManyToManyField(to='barcodeapp.Product'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='product',
        ),
        migrations.AddField(
            model_name='inspection',
            name='product',
            field=models.ManyToManyField(to='barcodeapp.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_issued_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 11, 16), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_received_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unity_of_measurement',
            field=models.CharField(choices=[('NUMBERS', 'NOS'), ('DOZEN', 'DZ'), ('PADS', 'PD'), ('SET', 'SET'), ('LEN', 'LEN'), ('KGS', 'KGS'), ('LIT', 'LIT'), ('BOT', 'BOT'), ('SQM', 'SQM'), ('PKT', 'PKT'), ('MTR', 'MTR'), ('BUN', 'BUN')], max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]

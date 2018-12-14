# Generated by Django 2.1.3 on 2018-12-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_no', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='lid',
            new_name='last_issued_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='lrd',
            new_name='last_received_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='expiry_date',
        ),
        migrations.AddField(
            model_name='exit',
            name='quantity_to_exit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

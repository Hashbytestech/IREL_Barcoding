# Generated by Django 2.1.3 on 2018-12-03 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0011_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_no', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='exit',
            name='product_requisition_no',
        ),
        migrations.AlterField(
            model_name='inspection',
            name='purchase_order_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barcodeapp.PurchaseOrder'),
        ),
        migrations.AddField(
            model_name='exit',
            name='purchase_order_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='barcodeapp.PurchaseOrder'),
            preserve_default=False,
        ),
    ]

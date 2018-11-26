# Generated by Django 2.1.3 on 2018-11-20 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rack',
            name='godown',
        ),
        migrations.AddField(
            model_name='shelf',
            name='godown',
            field=models.ForeignKey(db_column='Godown', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='barcodeapp.Godown'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-07-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_rename_warehouseproductstockhisory_warehouseproductstockhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseproductstockhistory',
            name='before_stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Before Stock(Pieces)'),
        ),
        migrations.AlterField(
            model_name='warehouseproductstockhistory',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Current Stock(Pieces)'),
        ),
    ]

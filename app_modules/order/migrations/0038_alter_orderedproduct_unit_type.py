# Generated by Django 4.1.7 on 2024-06-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0037_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='unit_type',
            field=models.CharField(default='piece', max_length=50, verbose_name='Unit Type'),
        ),
    ]

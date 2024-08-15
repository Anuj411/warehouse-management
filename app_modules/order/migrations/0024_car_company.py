# Generated by Django 4.1.7 on 2023-07-26 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_alter_warehouse_latitude_alter_warehouse_longitude'),
        ('order', '0023_merge_20230725_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='company',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='car_company', to='company.company', verbose_name='Company'),
            preserve_default=False,
        ),
    ]

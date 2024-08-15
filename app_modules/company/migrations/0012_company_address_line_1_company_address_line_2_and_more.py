# Generated by Django 4.1.7 on 2023-08-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_alter_warehouse_latitude_alter_warehouse_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='company',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='latitude',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company-logo', verbose_name='Company Logo'),
        ),
        migrations.AddField(
            model_name='company',
            name='longitude',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='company',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zip Code'),
        ),
    ]

# Generated by Django 4.1.7 on 2024-06-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0040_customerdiscount_brand_customerdiscount_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdiscount',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-09-27 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_remove_subcategory_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='genericname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Product Generic Name'),
        ),
    ]

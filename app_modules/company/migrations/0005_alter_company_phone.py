# Generated by Django 4.1.7 on 2023-06-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_status_warehouse_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number'),
        ),
    ]

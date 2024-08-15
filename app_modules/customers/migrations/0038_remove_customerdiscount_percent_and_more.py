# Generated by Django 4.1.7 on 2024-06-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0037_customerdiscount_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdiscount',
            name='percent',
        ),
        migrations.AddField(
            model_name='customerdiscount',
            name='discount',
            field=models.FloatField(blank=True, null=True, verbose_name='Discount'),
        ),
    ]

# Generated by Django 4.1.7 on 2024-07-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0060_orderbill_bill_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbill',
            name='bill_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Bill No'),
        ),
    ]

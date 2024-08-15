# Generated by Django 4.1.7 on 2023-07-07 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_status_alter_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_saved',
        ),
        migrations.AddField(
            model_name='order',
            name='internal_remarks',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Internal Remark'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Bill Date'),
        ),
    ]

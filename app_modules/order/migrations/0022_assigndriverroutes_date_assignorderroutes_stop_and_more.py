# Generated by Django 4.1.7 on 2023-07-24 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_merge_20230721_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigndriverroutes',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 11, 11, 21, 121533, tzinfo=datetime.timezone.utc), verbose_name='Deliver Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignorderroutes',
            name='stop',
            field=models.IntegerField(blank=True, null=True, verbose_name='stop'),
        ),
        migrations.DeleteModel(
            name='DriverAssignedOrders',
        ),
    ]

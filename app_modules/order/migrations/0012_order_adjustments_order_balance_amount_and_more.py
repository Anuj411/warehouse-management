# Generated by Django 4.1.7 on 2023-07-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adjustments',
            field=models.FloatField(blank=True, null=True, verbose_name='Adjustments'),
        ),
        migrations.AddField(
            model_name='order',
            name='balance_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Balance Amount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reference_number',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Reference Number'),
        ),
    ]

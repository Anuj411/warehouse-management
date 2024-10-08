# Generated by Django 4.1.7 on 2023-07-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0019_remove_order_billing_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderedproduct",
            name="packed_quantity",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Packed Quantity"
            ),
        ),
        migrations.AddField(
            model_name="orderedproduct",
            name="unpacked_quantity",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Unpacked Quantity"
            ),
        ),
    ]

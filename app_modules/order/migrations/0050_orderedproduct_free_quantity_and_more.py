# Generated by Django 4.1.7 on 2024-07-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0049_order_is_bill_generated_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproduct',
            name='free_quantity',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Free Quantity'),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='special_discount',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Special Discount'),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='special_rate',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Special Rate'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Gross Bill Total'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('dispatch', 'Dispatch'), ('new', 'New'), ('cancel', 'Cancel'), ('completed', 'Completed')], default='new', max_length=25, verbose_name='Status'),
        ),
    ]

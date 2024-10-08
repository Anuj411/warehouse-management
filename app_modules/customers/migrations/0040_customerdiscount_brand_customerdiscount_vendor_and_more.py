# Generated by Django 4.1.7 on 2024-06-17 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0011_alter_vendorpayment_payment_mode'),
        ('product', '0048_product_cost_price'),
        ('customers', '0039_multiplevendordiscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdiscount',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_brands', to='product.brand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='customerdiscount',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_discounts', to='vendors.vendor', verbose_name='Vendor'),
        ),
        migrations.AlterField(
            model_name='multiplevendordiscount',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_vendor_discounts', to='vendors.vendor', verbose_name='Vendor'),
        ),
    ]

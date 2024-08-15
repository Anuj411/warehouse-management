# Generated by Django 4.1.7 on 2024-06-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_alter_warehouse_company'),
        ('customers', '0036_customerdiscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdiscount',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_discounts', to='company.company', verbose_name='Company'),
        ),
    ]

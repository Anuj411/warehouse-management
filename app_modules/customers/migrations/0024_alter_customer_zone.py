# Generated by Django 4.1.7 on 2023-08-11 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0023_alter_customer_customer_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.zone', verbose_name='Zone'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-26 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_companyusers_user'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_orders', to='company.company'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-08-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0027_alter_customer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplecontact',
            name='contact_person',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='multiplecontact',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='multiplecontact',
            name='type',
            field=models.CharField(blank=True, choices=[('store', 'Store'), ('manager', 'Manager'), ('employee', 'Employee')], max_length=255, null=True, verbose_name='Type'),
        ),
    ]

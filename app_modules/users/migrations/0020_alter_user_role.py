# Generated by Django 4.1.7 on 2024-06-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('super admin', 'Super Admin'), ('company admin', 'Company Admin'), ('sales representative', 'Sales Representative'), ('driver', 'Driver'), ('accountant', 'Accountant')], default='admin', max_length=20, null=True, verbose_name='Role'),
        ),
    ]

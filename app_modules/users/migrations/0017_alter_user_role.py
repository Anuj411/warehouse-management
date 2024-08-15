# Generated by Django 4.1.7 on 2024-06-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_customerrorlogs_delete_errorlogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('super admin', 'Super Admin'), ('company admin', 'Company Admin'), ('sales representative', 'Sales Representative'), ('driver', 'Driver')], default='admin', max_length=20, null=True, verbose_name='Role'),
        ),
    ]

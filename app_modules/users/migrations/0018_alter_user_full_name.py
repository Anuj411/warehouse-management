# Generated by Django 4.1.7 on 2024-06-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='Full Name'),
        ),
    ]

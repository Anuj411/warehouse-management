# Generated by Django 4.1.7 on 2024-08-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0064_alter_assigndriverroutes_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='inform_admin_for_settlement',
            field=models.BooleanField(default=False, verbose_name='Inform Admin For Settlement'),
        ),
    ]

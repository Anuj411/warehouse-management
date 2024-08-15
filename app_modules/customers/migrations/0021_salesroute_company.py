# Generated by Django 4.1.7 on 2023-07-25 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_warehouse_city_alter_warehouse_country_and_more'),
        ('customers', '0020_merge_20230719_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesroute',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesroute_company', to='company.company'),
        ),
    ]

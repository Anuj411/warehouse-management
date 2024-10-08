# Generated by Django 4.1.7 on 2024-07-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_merge_20240709_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('dispatch', 'Dispatch'), ('new', 'New'), ('cancel', 'Cancel'), ('completed', 'Completed')], default='new', max_length=25, verbose_name='Status'),
        ),
    ]

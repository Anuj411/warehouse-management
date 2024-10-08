# Generated by Django 4.1.7 on 2024-07-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0048_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_bill_generated',
            field=models.BooleanField(default=False, verbose_name='Is Bill Generated'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('generate bill', 'Generate Bill'), ('dispatch', 'Dispatch'), ('new', 'New'), ('cancel', 'Cancel'), ('ready for dispatch', 'Ready For Dispatch'), ('completed', 'Completed')], default='new', max_length=25, verbose_name='Status'),
        ),
    ]

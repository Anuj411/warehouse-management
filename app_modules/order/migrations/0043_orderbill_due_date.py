# Generated by Django 4.1.7 on 2024-07-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0042_orderbill_slip_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbill',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Due Date'),
        ),
    ]

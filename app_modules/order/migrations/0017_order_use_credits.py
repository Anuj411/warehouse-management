# Generated by Django 4.1.7 on 2023-07-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_merge_20230717_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='use_credits',
            field=models.FloatField(blank=True, null=True, verbose_name='Use Credits'),
        ),
    ]

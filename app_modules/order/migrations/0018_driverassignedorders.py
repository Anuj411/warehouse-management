# Generated by Django 4.1.7 on 2023-07-20 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_driver'),
        ('order', '0017_order_use_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverAssignedOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('date', models.DateField(verbose_name='Deliver Date')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_assign_orders', to='users.driver', verbose_name='Assign Driver')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_order', to='order.order', verbose_name='Assign Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

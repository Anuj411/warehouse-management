# Generated by Django 4.1.7 on 2024-06-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_merge_0014_alter_user_managers_0014_errorlogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomErrorLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('url', models.CharField(max_length=1000, verbose_name='URL')),
                ('logs', models.TextField(verbose_name='Logs')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='ErrorLogs',
        ),
    ]

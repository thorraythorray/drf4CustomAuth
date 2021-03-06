# Generated by Django 4.0.1 on 2022-01-17 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScanTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_tm', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_tm', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('system_id', models.IntegerField(default=0, verbose_name='系统ID')),
                ('scan_id', models.CharField(max_length=128, verbose_name='扫描ID')),
                ('ips', models.CharField(max_length=256, verbose_name='扫描的网段')),
                ('ports', models.CharField(max_length=256, verbose_name='扫描的端口')),
                ('more', models.TextField()),
            ],
            options={
                'ordering': ['update_tm'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-22 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoredItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitored_type', models.CharField(help_text='监控项目', max_length=3)),
                ('content', models.CharField(help_text='监控的子项', max_length=255)),
                ('describe', models.CharField(default=None, help_text='描述', max_length=200, null=True)),
                ('is_active', models.CharField(help_text='是否启用', max_length=1)),
                ('memo', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='监控大项', max_length=100)),
                ('choice', models.CharField(help_text='类型', max_length=3)),
                ('is_active', models.CharField(help_text='是否启用', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ServerAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(help_text='登录账户', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServerError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now=True, help_text='开始时间')),
                ('end_time', models.DateTimeField(default=True, help_text='结束时间', null=True)),
                ('error_type', models.CharField(help_text='错误的类型', max_length=3)),
                ('describe', models.CharField(default=None, help_text='描述', max_length=200, null=True)),
                ('error_code', models.CharField(help_text='错误代码', max_length=10)),
                ('error_level', models.CharField(help_text='错误等级', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_id', models.CharField(help_text='服务器标志', max_length=100)),
                ('name', models.CharField(help_text='服务器名称', max_length=100)),
                ('system_type', models.CharField(default='linux', max_length=100)),
                ('is_active', models.CharField(default=1, help_text='是否监控', max_length=2)),
                ('creator', models.CharField(default='sys', help_text='创建人', max_length=100)),
                ('created_time', models.DateTimeField(auto_now=True, help_text='加入时间')),
                ('updater', models.CharField(default=None, help_text='更新人', max_length=100, null=True)),
                ('update_time', models.DateTimeField(default=None, help_text='更新时间', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServerItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.CharField(help_text='是否启用', max_length=1)),
                ('server_i', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_m_i', to='server_info.MonitoredItems')),
            ],
        ),
        migrations.CreateModel(
            name='ServerMonitored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitored_type', models.CharField(help_text='监控项目', max_length=3)),
                ('frequency', models.IntegerField(default=60, help_text='监控频率(秒)')),
                ('is_active', models.CharField(help_text='是否启用', max_length=1)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_monitored', to='server_info.ServerInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ServerRights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('describe', models.CharField(max_length=100)),
                ('is_active', models.CharField(help_text='是否启用', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ServerWarn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warn_type', models.CharField(help_text='警告类型', max_length=3)),
                ('describe', models.CharField(help_text='警告信息', max_length=255)),
                ('warn_detail', models.TextField(default=None, help_text='详细信息', null=True)),
                ('created_time', models.DateTimeField(auto_now=True, help_text='加入时间')),
                ('end_time', models.DateTimeField(default=None, null=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_warn', to='server_info.ServerInfo')),
            ],
        ),
        migrations.AddField(
            model_name='serveritems',
            name='server_m',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_s_m', to='server_info.ServerMonitored'),
        ),
        migrations.AddField(
            model_name='servererror',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_error', to='server_info.ServerInfo'),
        ),
        migrations.AddField(
            model_name='serveradmin',
            name='rights',
            field=models.ManyToManyField(related_name='my_rights', to='server_info.ServerRights'),
        ),
        migrations.AddField(
            model_name='serveradmin',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_user', to='server_info.ServerInfo'),
        ),
    ]
from django.db import models

# Create your models here.
monitored_type_choice = (
        ('0', 'CPU'),
        ('1', '内存'),
        ('2', '硬盘'),
        ('4', '网络'),
        ('5', '系统'),
        ('6', '进程'),
        ('7', '端口'),
    )


# 基本信息表
class ServerInfo(models.Model):
    server_id = models.CharField(max_length=100, help_text='服务器标志')
    name = models.CharField(max_length=100, help_text='服务器名称')
    system_type = models.CharField(max_length=100, default='linux')
    # 0 不监控，1 监控
    is_active = models.CharField(max_length=2, help_text='是否监控', default=1)
    creator = models.CharField(max_length=100, help_text='创建人', default='sys')
    created_time = models.DateTimeField(auto_now=True, help_text='加入时间')
    updater = models.CharField(max_length=100, help_text='更新人', default=None, null=True)
    update_time = models.DateTimeField(help_text='更新时间', default=None, null=True)


# 服务器权限
class ServerRights(models.Model):
    name = models.CharField(max_length=100)
    describe = models.CharField(max_length=100)
    is_active = models.CharField(max_length=1, help_text='是否启用')


# 每账号对应的服务器权限
class ServerAdmin(models.Model):
    server = models.ForeignKey(ServerInfo, related_name='my_user')
    user = models.CharField(max_length=100, help_text='登录账户')
    rights = models.ManyToManyField(ServerRights, related_name='my_rights')

# 操作日志表, 暂无


# 系统错误表
class ServerError(models.Model):
    server = models.ForeignKey(ServerInfo, related_name='my_error')
    start_time = models.DateTimeField(auto_now=True, help_text='开始时间')
    end_time = models.DateTimeField(help_text='结束时间', default=True, null=True)
    error_type = models.CharField(max_length=3, help_text='错误的类型')
    describe = models.CharField(max_length=200, help_text='描述', default=None, null=True)
    error_code = models.CharField(max_length=10, help_text='错误代码')
    error_level = models.CharField(max_length=3, help_text='错误等级')


# 系统告警表
class ServerWarn(models.Model):
    server = models.ForeignKey(ServerInfo, related_name='my_warn')
    warn_type = models.CharField(max_length=3, help_text='警告类型')
    describe = models.CharField(max_length=255, help_text='警告信息')
    warn_detail = models.TextField(help_text='详细信息', default=None, null=True)
    created_time = models.DateTimeField(auto_now=True, help_text='加入时间')
    end_time = models.DateTimeField(default=None, null=True)


class MonitorType(models.Model):
    name = models.CharField(max_length=100, help_text='监控大项')
    monitor_choice = (
        ('1', '硬件'),
        ('2', 'WEB应用'),
        ('3', '数据库'),

    )
    choice = models.CharField(max_length=3, help_text='类型')
    is_active = models.CharField(max_length=1, help_text='是否启用')


# 监控细项表
class MonitoredItems(models.Model):
    monitored_type = models.CharField(max_length=3, help_text='监控项目')
    content = models.CharField(max_length=255, help_text='监控的子项')
    describe = models.CharField(max_length=200, help_text='描述', default=None, null=True)
    is_active = models.CharField(max_length=1, help_text='是否启用')
    memo = models.CharField(max_length=200, default=None, null=True)


#
class ServerMonitored(models.Model):
    server = models.ForeignKey(ServerInfo, related_name='my_monitored')
    monitored_type = models.CharField(max_length=3, help_text='监控项目')
    frequency = models.IntegerField(help_text='监控频率(秒)', default=60)
    is_active = models.CharField(max_length=1, help_text='是否启用')


class ServerItems(models.Model):
    server_m = models.ForeignKey(ServerMonitored, related_name='my_s_m')
    server_i = models.ForeignKey(MonitoredItems, related_name='my_m_i')
    is_active = models.CharField(max_length=1, help_text='是否启用')




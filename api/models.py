import hashlib
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码", max_length=64)
    uid = models.CharField(verbose_name='个人唯一ID', max_length=64, unique=True)
    wx_id = models.CharField(verbose_name="微信ID", max_length=128, blank=True, null=True, db_index=True)

    def save(self, *args, **kwargs):
        # 创建用户时，为用户自动生成个人唯一ID
        if not self.pk:
            m = hashlib.md5()
            m.update(self.username.encode(encoding="utf-8"))
            self.uid = m.hexdigest()
        super(User, self).save(*args, **kwargs)


class UserToken(models.Model):
    user = models.ForeignKey(to="User")
    token = models.CharField(max_length=32)


class Device(models.Model):
    dev_id = models.CharField(verbose_name="设备ID", max_length=16, unique=True)
    status_choice = (
        (1, "在线"),
        (2, "离线"),
    )
    status = models.IntegerField(verbose_name="设备状态", choices=status_choice)
    ICCID = models.CharField(verbose_name="设备ICCID", max_length=32, unique=True)
    IC_Card = models.CharField(verbose_name="物联网卡号", max_length=16)
    type = models.IntegerField(verbose_name="设备种类")
    goods = models.ManyToManyField(to="Goods")


class Receive(models.Model):
    msg_id = models.CharField(max_length=16)
    dev_id = models.CharField(max_length=16)
    cmd_choice = (
        ("online", "设备上线"),
        ("offline", "设备离线"),
        ("test", "数据订阅接口验证"),
        ("41", "RTU上报数据"),
        ("42", "平台下发数据返回结果"),
    )
    cmd = models.CharField(max_length=16, choices=cmd_choice)
    data = models.CharField(max_length=512, null=True, blank=True)


class Send(models.Model):
    msg_id = models.CharField(max_length=16)
    dev_id = models.CharField(max_length=16)
    token = models.CharField(max_length=32)
    data = models.CharField(max_length=512)
    recode_choice = (
        (0, "成功"),
        (1001, "token不能为空"),
        (1002, "设备ID不能为空"),
        (1003, "消息ID不能为空"),
        (1004, "消息ID错误"),
        (1005, "token验证失败"),
        (1007, "设备已离线"),
        (1006, "设备ID验证失败"),
        (3000, "socket服务器错误"),
    )
    recode = models.IntegerField(choices=recode_choice)


class Goods(models.Model):
    title = models.CharField(verbose_name="商品名称", max_length=32)
    old_price = models.FloatField(verbose_name="商品原价")
    new_price = models.FloatField(verbose_name="商品现价")
    desc = models.CharField(verbose_name="商品描述", max_length=256)





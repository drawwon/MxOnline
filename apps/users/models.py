from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name='昵称',default='')
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='',verbose_name='性别')
    address = models.CharField(max_length=100,default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',verbose_name='照片')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name= '邮箱')
    send_type = models.CharField(choices=(('register','注册'),('forget','找回密码')),max_length=10,verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now,verbose_name='发送时间') #记得去掉datetime.now的括号，不然只会记录class生成的时间
    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')
    url = models.URLField(max_length=500, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


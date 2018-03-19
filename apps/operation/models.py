from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import Course
from organization.models import CourseOrg


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50,verbose_name='课程名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.PROTECT, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.PROTECT,verbose_name='课程')
    comments = models.CharField(max_length=500,verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT,verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1,'课程'),(2,'课程机构'),(3,'讲师')),default=1,verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name='接收用户')# 不用外键，因为有可能是发给所有人的消息，用0表示发送给所有人的消息,用int表示用户的id
    message = models.CharField(max_length=500, verbose_name='消息内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    has_read = models.BooleanField(default=False,verbose_name='是否已读')
    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT,verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.PROTECT,verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


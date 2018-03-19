from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('cj','初级'),('zj','中级'),('gj','高级')),verbose_name='课程难度',max_length=2)
    learn_time = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='课程'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.PROTECT,verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT,verbose_name='课程')
    download = models.FileField(upload_to='courses/resource/%Y/%m',max_length=100)
    name = models.CharField(max_length=100, verbose_name='资源名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name


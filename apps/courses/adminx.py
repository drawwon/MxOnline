#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 11:25
import xadmin
from courses.models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students','fav','image','click_num','add_time']
    search_fields = ['name','desc','detail','degree','learn_time','students','fav','image','click_num','add_time']
    list_filter = ['name','desc','detail','degree','learn_time','students','fav','image','click_num','add_time']

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name','add_time']
    list_filter = ['course__name','name','add_time']

class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name','add_time']
    list_filter = ['lesson','name','add_time']

class CourseResourceAdmin(object):
    list_display = ['course','download','name','add_time']
    search_fields = ['course','download','name','add_time']
    list_filter = ['course','download','name','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

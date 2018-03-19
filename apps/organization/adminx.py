#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 16:24

import xadmin
from organization.models import CourseOrg,CityDict,Teacher

class CourseOrgAdmin:
    list_display = ['city','name','desc','click_nums','fav_nums','image','address','add_time']
    search_fields = ['city','name','desc','click_nums','fav_nums','image','address']
    list_filter = ['city','name','desc','click_nums','fav_nums','image','address','add_time']

class CityDictAdmin:
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc','add_time']

class TeacherAdmin:
    list_display = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']

xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)

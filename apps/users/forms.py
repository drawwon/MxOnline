#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 19:24

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)#,error_messages={'invalid':'请输入一个有效的邮箱地址'})
    password = forms.CharField(required=True,min_length=5,error_messages={'invalid':'密码至少6个字符','required':'请输入密码'})
    captcha = CaptchaField(error_messages={'required': '验证码错误'})

class ForgetPwdForm(forms.Form):
    # username = forms.EmailField(required=True,error_messages={'required':'账号输入有误'})
    email = forms.EmailField(required=True)#,error_messages={'invalid':'请输入一个有效的邮箱地址'})
    captcha = CaptchaField(error_messages={'required': '验证码错误'})

class ResetPwdForm(forms.Form):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

# coding: utf-8
import json
import logging
from django import forms
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.views.decorators.csrf import ensure_csrf_cookie
from django_render_json import json, render_json
from promotion.models import *
from students.models import *
import urllib
import urllib2


#接口地址

def api_post(url,data):
	url = "http://demovoice.jdb.cn"
	req = urllib2.Request(url)
	data = urllib.urlencode(data)
	response = opener.open(req, data)
	return response.read() 

def getVboard():
	#获取最V榜单三个人
	whereurl = "/Api/GetPeriodStudents.aspx"
	data = {"period":1,"keyword":"","start":1,"end":5}
	res = api_post(url+whereurl,data)
	print (res)
	#try:
	#	res = Student.objects.order_by('id')[0:3]
	#	print "None"
	return res

def check_pro_num():
	return True


def check_pro_num_mobile():
	#查看手机+罐码组合
	return True

def getStudents():
	#获取所有学院信息
	try:
		res = Student.objects.all()
	except Student.DoesNotExist:
		print "None"
	return res


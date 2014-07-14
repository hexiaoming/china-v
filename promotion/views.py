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
import re
import time
from promotion.models import *
from promotion.do import *
# Create your views here.
@require_GET
def index(request):
	if request.method == 'GET':
		return render(request,"promotion/promotion.html")
@ensure_csrf_cookie
@require_GET

def provet(request):
	if request.method == 'GET':
		return render(request,"promotion/provet.html")

@require_GET
def mobvet(request):
	if request.method == 'GET':
		return render(request,"promotion/mobvet.html")

@require_POST
@ensure_csrf_cookie
def mobvet_post(request):
	if request.method == 'POST':
		mobile = request.POST.get('mobile',None)
		m = Mobvet.objects.create(mobile=str(mobile),timestamp=str(time.time()))
		m.save()
		try:
			q =	student.objects.all()

		except student.DoesNotExist:
			return render_json({"reason":"no students please import data"})
		return render(request,"promotion/Vboard.html",{"dovet":"mob","result":q})
	else:
		return render(request,"promotion/proerror.html")

@require_GET
def instruction(request):
	if request.method == 'GET':
		return render(request,"promotion/instruction.html")

@require_GET
def Vboard(request):
	if request.method == 'GET':
		try:
			q =	student.objects.all()
		except student.DoesNotExist:
			return render_json({"reason":"no students please import data"})
		return render(request,"promotion/Vboard.html",{"dovet":"dir","result":q})

@require_GET
def proerror(request):
	if request.method == 'GET':
		return render(request,"promotion/proerror.html")

@require_POST
@ensure_csrf_cookie
def pro_mobvet(request):
	#此页面只允许使用post的方式进行访问，如果方式有问题，则返回错误页面
	if request.method == 'POST':
		circle = request.POST.get('circle',None)
		top = request.POST.get('top',None)
		#罐投票验证
		if check_pro_num():
			return render(request,"promotion/pro_mobvet.html",{"circle":str(circle),"top":str(top)})
		else:
			return render(request,"/promotion/proerror/")
	else:
		return redirect("/promotion/proerror/")

@require_POST	
@ensure_csrf_cookie
def vet(request):
	#此页面只允许使用post的方式进行访问，如果方式有问题，则返回错误页面
	if request.method == 'POST':
		mobile = request.POST.get('mobile',None)
		circle = request.POST.get('circle',None)
		top = request.POST.get('top',None)
		timestamp = time.time()
		if check_pro_num_mobile():
			p = Provet.objects.create(circle_num=str(circle),top_num=str(top),mobile=str(mobile),timestamp=str(timestamp))
			p.save()
			try:
				q =	student.objects.all()
			except student.DoesNotExist:
				return render_json({"reason":"no students please import data"})
			return render(request,"promotion/Vboard.html",{"dovet":"pro"})
		else:
			return redirect("/promotion/proerror/")
	else:
		return redirect("/promotion/proerror/")


@require_GET
def vboard_show(request):
	#这个是显示最V榜单
	res = getVboard()
	return render(request,"promotion/vboard_show.html",{"res":res})

@require_GET
def studentlist(request):
	#学员展示页面
	studentlist = getStudents()
	return render(request,"promotion/studentlist.html",{"studentlist":studentlist})
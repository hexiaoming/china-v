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

@require_GET
def instruction(request):
	if request.method == 'GET':
		return render(request,"promotion/instruction.html")

@require_GET
def Vboard(request):
	if request.method == 'GET':
		return render(request,"promotion/Vboard.html")

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
			#展示填写手机信息页面，并把circle，top，传入模板作为hidden的元素
		return render(request,"promotion/pro_mobvet.html",{"circle":circle,"top":top})
	else:
		return redirect("/promotion/proerror/")

@require_POST
@ensure_csrf_cookie
def vet(request):
	#此页面只允许使用post的方式进行访问，如果方式有问题，则返回错误页面
	if request.method == 'POST':
		mobile = request.POST.get('mobile',None)
		return render(request,"promotion/Vboard.html",{"dovet":"pro"})
	else:
		return redirect("/promotion/proerror/")	
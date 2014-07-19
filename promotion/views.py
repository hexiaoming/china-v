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
from promotion.do import *
from itertools import chain
# Create your views here.
logger = logging.getLogger(__name__)

@require_GET
def index(request):
	request.session.clear()	

	if request.method == 'GET':
		student = getStudents(1)
		studentlist = student['Data']
		
		Address = "http://voice.jdb.cn"
		c = 0
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
		studentlist = studentlist[0:3]
		for i in studentlist:
			c += 1
			i['ranked'] = c 
		return render(request,"promotion/promotion.html",{"studentlist":studentlist})

@require_GET
def getFirstThree(request):

	if request.method == 'GET':
		student = getStudents(1)
		studentlist = student['Data']
		
		Address = "http://voice.jdb.cn"
		c = 0
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
		studentlist = studentlist[0:3]
		for i in studentlist:
			c += 1
			i['ranked'] = c 
		return render(request,"promotion/promotion.html",{"studentlist":studentlist})

@ensure_csrf_cookie
@require_GET

def provet(request):
	if request.method == 'GET':
		return render(request,"promotion/provet.html")

@require_GET
def mobvet(request):
	if request.method == 'GET':
		return render(request,"promotion/mobvet.html")


@ensure_csrf_cookie
def mobvet_post(request):
	if request.method == 'POST':

		mobile = request.POST.get('mobile',None)
		#log打出手机号
		
		request.session['mobile']=str(mobile)
		logger.warn(mobile)
		return render(request,"promotion/Vboard.html",{"dovet":"mob"})
	else:
		
		student = getStudents(1)
		studentlist = student['Data']
		c = 1
		studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
		
		studentlist = studentlist[c::]+studentlist[0:c]
		Address = "http://voice.jdb.cn"
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		return render(request,"promotion/studentlist.html",{"dovet":"mob","studentlist":studentlist})

@require_GET
def instruction(request):
	if request.method == 'GET':
		return render(request,"promotion/instruction.html")

def postticket(request):
	StudentId = request.POST.get('StudentId') ;
	openID = request.POST.get('openID')
	res = votes(openID,StudentId);
	if res == 1 :
		return render(request,"promotion/vote_success.html")
	else :
		#返回错误页面
		return render(request,"promotion/vote_filed.html")

@require_GET
def Vboard(request,studentid):
	if request.method == 'GET':
		student = getStudents(1)
		studentlist = student['Data']
		c = 1
		studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
		for i in studentlist:
			if str(i['StudentId']) == str(studentid):
				break
			c += 1

		studentlist = studentlist[c::]+studentlist[0:c]
		Address = "http://voice.jdb.cn"
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		mobile = request.session.get('mobile')
		top = request.session.get('top')
		circle = request.session.get('circle')
		if None == mobile and None == top and None == circle:
			return render(request,"promotion/Vboard.html",{"dovet":"dir","studentid":studentid,"studentlist":studentlist})
		elif None != mobile and None == top and None == circle:	
			return render(request,"promotion/Vboard.html",{"dovet":"mob","studentid":studentid,"studentlist":studentlist})
		elif None != mobile and None != top and None != circle:
			return render(request,"promotion/Vboard.html",{"dovet":"pro","studentid":studentid,"studentlist":studentlist})

		


@require_GET
def proerror(request):
	if request.method == 'GET':
		return render(request,"promotion/proerror.html")
@require_GET
def proerror_mobile(request):
	if request.method == 'GET':
		return render(request,"promotion/proerror_mobile.html")
@require_GET
def error_mobile(request):
	if request.method == 'GET':
		return render(request,"promotion/error_mobile.html")

@require_POST
@ensure_csrf_cookie
def pro_mobvet(request):
	#此页面只允许使用post的方式进行访问，如果方式有问题，则返回错误页面
	if request.method == 'POST':
		circle = request.POST.get('circle',None)
		top = request.POST.get('top',None)
		openID = request.POST.get('openID',None)
		#罐投票验证
		#Status=-1，接口异常
	    #Status=0，参数不全
	    #Status=1，增加投票权成功
	    #Status=2，3位码或8位码错误
	    #Status=3，已经使用
		if check_pro_num(openID,circle,top)==1:
			return render(request,"promotion/pro_mobvet.html",{"circle":str(circle),"top":str(top)})
		else:
			return redirect("/promotion/proerror/")
	else:
		return redirect("/promotion/proerror/")

	
@ensure_csrf_cookie
def vet(request,studentid):
	if request.method == 'POST':
		mobile = request.POST.get('mobile',None)
		circle = request.POST.get('circle',None)
		top = request.POST.get('top',None)
		openID = request.POST.get('openID',None)
		timestamp = time.time()
		#存session
		request.session['mobile']=str(mobile)
		request.session['top']=str(top)
		request.session['circle']=str(circle)
		#结束
		if check_pro_num_mobile(openID):	
			student = getStudents(1)
			studentlist = student['Data']
			c = 1
			studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
			for i in studentlist:
				if str(i['StudentId']) == str(studentid):
					break
				c+=1
			studentlist = studentlist[c::]+studentlist[0:c]
			Address = "http://voice.jdb.cn"
			for i in studentlist:
				i['Avatar'] = Address + i['Avatar']
			return render(request,"promotion/studentlist.html",{"dovet":"pro","studentlist":studentlist})
		else:
			return redirect("/promotion/proerror/")
	else:
		mobile = request.session.get('mobile')
		top = request.session.get('top')
		circle = request.session.get('circle')
		#用log打出手机号
		logger.warn(mobile)
		if ""==mobile:
			return redirect("/promotion/proerror/")
		elif ""==top or ""==circle:
			return redirect("/promotion/proerror/")
		else:
			#跳回本页面
			student = getStudents(1)
			studentlist = student['Data']
			c = 1
			studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
			for i in studentlist:
				if str(i['StudentId']) == str(studentid):
					break
				c+=1
			studentlist = studentlist[c::]+studentlist[0:c]
			Address = "http://voice.jdb.cn"
			for i in studentlist:
				i['Avatar'] = Address + i['Avatar']
			return render(request,"promotion/studentlist.html",{"dovet":"pro","studentlist":studentlist})

@require_POST
def getticket(request):
	sid = request.POST.get("sid")
	res = getTicket(sid)
	vote = res['Data']['Votes']
	if res['Status']==1:
		return render_json({"vote":vote})
	else:
		return render_json({"vote":0})

@require_GET
def vboard_show(request):
	#这个是显示最V榜单
	res = getVboard()
	return render(request,"promotion/vboard_show.html",{"res":res})

@require_GET
def studentlist(request):
	#学员展示页面
	mobile = request.session.get('mobile')
	circle = request.session.get('circle')
	top = request.session.get('top')
	student = getStudents(1)
	studentlist = student['Data']
	Address = "http://voice.jdb.cn"
	for i in studentlist:
		i['Avatar'] = Address + i['Avatar']
	studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
	return render(request,"promotion/studentlist.html",{"studentlist":studentlist,"type":"none","mobile":mobile,"circle":circle,"top":top})
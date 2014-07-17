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
def index(request,openID):
	request.session.clear()	
	if request.method == 'GET':
		student = getStudents(1)
		studentlist = student['Data']
		studentlist = studentlist[0:3]
		Address = "http://demovoice.jdb.cn"
		c = 0
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
		for i in studentlist:
			c += 1
			i['ranked'] = c 
		return render(request,"promotion/promotion.html",{"studentlist":studentlist,"openID":openID})

@ensure_csrf_cookie
@require_GET

def provet(request,openID):
	if request.method == 'GET':
		return render(request,"promotion/provet.html",{"openID":openID})

@require_GET
def mobvet(request,openID):
	if request.method == 'GET':
		return render(request,"promotion/mobvet.html",{"openID":openID})


@ensure_csrf_cookie
def mobvet_post(request,openID):
	if request.method == 'POST':
		#log打出手机号

		mobile = request.POST.get('mobile',None)
		request.session['mobile']=str(mobile)
		return render(request,"promotion/Vboard.html",{"dovet":"mob","openID":openID})
	else:
		
		student = getStudents(1)
		studentlist = student['Data']
		c = 1
		studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
		
		studentlist = studentlist[c::]+studentlist[0:c]
		Address = "http://demovoice.jdb.cn"
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		return render(request,"promotion/Vboard.html",{"dovet":"mob","studentlist":studentlist,"openID":openID})

@require_GET
def instruction(request,openID):
	if request.method == 'GET':
		return render(request,"promotion/instruction.html")
def postticket(request,openID):
	StudentId = request.POST.get('StudentId') ;
	res = votes(openID,StudentId);
	if res == 1 :
		return render(request,"promotion/vote_success.html",{"openID":openID})
	else :
		#返回错误页面
		return render(request,"promotion/vote_filed.html",{"openID":openID})
@require_GET
def Vboard(request,studentid,openID):
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
		Address = "http://demovoice.jdb.cn"
		for i in studentlist:
			i['Avatar'] = Address + i['Avatar']
		return render(request,"promotion/Vboard.html",{"dovet":"dir","studentid":studentid,"studentlist":studentlist,"openID":openID})

@require_GET
def proerror(request,openID):
	if request.method == 'GET':
		return render(request,"promotion/proerror.html")
@require_GET
def proerror_mobile(request,openID):
	if request.method == 'GET':
		return render(request,"promotion/proerror_mobile.html")
@require_GET
def error_mobile(request,openID):
	if request.method == 'GET':
		return render(request,"promotion/error_mobile.html")

@require_POST
@ensure_csrf_cookie
def pro_mobvet(request,openID):
	#此页面只允许使用post的方式进行访问，如果方式有问题，则返回错误页面
	if request.method == 'POST':
		circle = request.POST.get('circle',None)
		top = request.POST.get('top',None)
		#罐投票验证
		#Status=-1，接口异常
	    #Status=0，参数不全
	    #Status=1，增加投票权成功
	    #Status=2，3位码或8位码错误
	    #Status=3，已经使用
		if check_pro_num(openID,circle,top)==1:
			return render(request,"promotion/pro_mobvet.html",{"circle":str(circle),"top":str(top),"openID":openID})
		else:
			return redirect("/promotion/proerror/"+openID+"/")
	else:
		return redirect("/promotion/proerror/"+openID+"/")

	
@ensure_csrf_cookie
def vet(request,studentid,openID):
	if request.method == 'POST':
		mobile = request.POST.get('mobile',None)
		circle = request.POST.get('circle',None)
		top = request.POST.get('top',None)
		timestamp = time.time()
		#存session
		request.session['mobile']=str(mobile)
		request.session['top']=str(top)
		request.session['circle']=str(circle)
		#结束
		if check_pro_num_mobile():	
			student = getStudents(1)
			studentlist = student['Data']
			c = 1
			studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
			for i in studentlist:
				if str(i['StudentId']) == str(studentid):
					break
				c+=1
			studentlist = studentlist[c::]+studentlist[0:c]
			Address = "http://demovoice.jdb.cn"
			for i in studentlist:
				i['Avatar'] = Address + i['Avatar']
			return render(request,"promotion/Vboard.html",{"dovet":"pro","studentlist":studentlist,"openID":openID})
		else:
			return redirect("/promotion/proerror/"+openID+"/")
	else:
		mobile = request.session.get('mobile')
		top = request.session.get('top')
		circle = request.session.get('circle')
		#用log打出手机号
		logger.warn(mobile)
		if ""==mobile:
			return redirect("/promotion/proerror/"+openID+"/")
		elif ""==top or ""==circle:
			return redirect("/promotion/proerror/"+openID+"/")
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
			Address = "http://demovoice.jdb.cn"
			for i in studentlist:
				i['Avatar'] = Address + i['Avatar']
			return render(request,"promotion/Vboard.html",{"dovet":"pro","studentlist":studentlist,"openID":openID})

@require_GET
def vboard_show(request,openID):
	#这个是显示最V榜单
	res = getVboard()
	return render(request,"promotion/vboard_show.html",{"res":res,"openID":openID})

@require_GET
def studentlist(request,openID):
	#学员展示页面
	mobile = request.session.get('mobile')
	circle = request.session.get('circle')
	top = request.session.get('top')
	student = getStudents(1)
	studentlist = student['Data']
	Address = "http://demovoice.jdb.cn"
	for i in studentlist:
		i['Avatar'] = Address + i['Avatar']
	studentlist.sort(lambda x,y: cmp(y['Votes'],x['Votes']))
	return render(request,"promotion/studentlist.html",{"studentlist":studentlist,"type":"none","mobile":mobile,"circle":circle,"top":top,"openID":openID})
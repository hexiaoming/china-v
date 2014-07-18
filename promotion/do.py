# coding: utf-8

import logging
from django import forms
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.views.decorators.csrf import ensure_csrf_cookie
from promotion.models import *
from students.models import *
import urllib
import urllib2
import json
#接口地址

def api_post(whereurl,data):
    url = "http://demovoice.jdb.cn/" + whereurl
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    Json = urllib2.urlopen(url,data)
    res = Json.read()
    res = res.split("<!DOCTYPE")
    s = res[0].replace('\r\n','')
    s = json.loads(s)
    return s

def getVboard():
    #获取最V榜单三个人
    whereurl = "/Api/GetPeriodStudents.aspx"
    data = {"period":1,"keyword":"","start":1,"end":5}
    res = api_post(whereurl,data)
    return res

def getTicket(sid):
    whereurl = "/Api/GetStudent.aspx"
    data = {"sid":sid}
    res = api_post(whereurl,data)
    return res
def check_pro_num(openID,ring,Can):
	#查看手机+罐码组合
	#调用接口二，为用户提供
    #从url get到用户openID
    ##openID 未定义 由url中get取得###
    whereurl = "/Api/AddUserVotes.aspx"
    data = {"uid":openID,"ring":ring,"Can":Can}
    res = api_post(whereurl , data)
    
    return res['Status']

def getStudents(period):
	#获取本期所有学员信息
    whereurl = "/Api/GetPeriodStudents.aspx"
    data = {"period":period,"keyword":"","start":1,"end":30}
    res = api_post(whereurl,data)
    return res

def votes(openID,sid):
    #为id的学员投票
    #Status=-1，接口异常
    #Status=0，参数不全
    #Status=1，投票成功
    #Status=2，不存在的学员
    #Status=3，投票权限不足
    whereurl = "/Api/AddStudentVotes.aspx"
    data = {"uid":openID,"sid":sid}
    res = api_post(whereurl,data)
    return res['Status']

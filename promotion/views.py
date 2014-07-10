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
# Create your views here.
@require_GET
def index(request):
	if request.method == 'GET':
		return render(request,"promotion/promotion.html")

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
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


logger = logging.getLogger(__name__)


@require_GET
def welcome(request):
    if not request.user.is_authenticated():
        logger.warn("welcome: user is not authenticated")
        return redirect("/login")
    else:
        return redirect("/backend/")


@require_GET
def index(request):
    return render_json({'content': 'hello!'});


@require_GET
def logout(request):
    auth.logout(request)
    return redirect("/welcome")


@require_http_methods(['GET', 'POST'])
@ensure_csrf_cookie
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)

        if not user:
            return render_json({'ret_code': 1})

        auth.login(request, user)
        return render_json({'ret_code': 0})


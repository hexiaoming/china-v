#coding: utf8
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie


@require_GET
def index(request):
    return render(request, "shake/index.html")


@require_GET
@ensure_csrf_cookie
def vote(request):
    return render(request, "shake/vote.html")
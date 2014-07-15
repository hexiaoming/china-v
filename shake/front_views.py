#coding: utf8
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie

from students.models import Student

@require_GET
def index(request):
    student = Student.objects.getPlayingStudent();
    return render(request, "shake/index.html", {
        'vote': student.getVote() if student else None
    })


@require_GET
def rank(request):
    return render(request, "shake/rank.html")
    

@require_GET
def lottery(request):
    return render(request, "shake/lottery.html")
    
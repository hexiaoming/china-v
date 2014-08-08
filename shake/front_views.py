#coding: utf8
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie

from students.models import Student

@require_GET
def index(request):
    student = Student.objects.getPlayingStudent()
    return render(request, "shake/index.html", {
        'playing': 'true' if student else 'false',
        'vote': 0 #student.getVote() if student else None
    })


@require_GET
def rank(request):
    students = Student.objects.all();
    return render(request, "shake/rank.html", {
        'students': students
    })
    

@require_GET
def lottery(request):
    student = Student.objects.getPlayingStudent()
    return render(request, "shake/lottery.html", {
        'playing': 'true' if student else 'false'
    })
    

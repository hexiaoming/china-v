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

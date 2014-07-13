#coding: utf-8
import logging

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from django_tables2 import RequestConfig 
from django.utils.safestring import mark_safe
from django_render_json import json as as_json
import django_tables2 as tables
import django_active_tab as active_tab
from django import forms

from students.models import Student
from ajax_upload.widgets import AjaxClearableFileInput

logger = logging.getLogger(__name__)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'parsley-required': 'true'
            }),
            'avatar': AjaxClearableFileInput(attrs={
                'class': 'form-control',
                'parsley-required': 'true'
            })
        }


class StudentTable(tables.Table):
    ops = tables.columns.TemplateColumn(verbose_name=u'操作', template_name='student_ops.html', orderable=False)

    def render_avatar(request, value):
        return mark_safe("<a href='%s'><img class='img-thumbnail' src='%s'></a>" % (value, value))

    class Meta:
        model = Student
        fields=("name", "avatar")
        empty_text = u'暂无学员信息'
        orderable=False
        attrs = {
            'class': 'table table-bordered table-striped'
        }


@require_GET
@login_required
@active_tab("students")
def index(request):
    data = Student.objects.all().order_by('-pk');

    query = request.GET.get("q", None);
    searching = query is not None
    if searching:
        if query == '':
            return redirect('/backend/students/')
        data = data.filter(name__contains=query)

    table = StudentTable(data)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    if searching:
        table.empty_text = u'没有搜索结果'

    return render(request, "students.html", {
        'table': table,
        'form': StudentForm()
    })


@require_POST
@as_json
def add_student(request):
    form = StudentForm(request.POST)
    if not form.is_valid():
        logger.warn("form is invalid");
        logger.warn("erros");
        logger.warn(form.errors);
        return { 'ret_code': 1002 }

    form.save()
    return { 'ret_code': 0}


@require_POST
@as_json
def edit_student(request):
    pk = request.POST.get("pk", None)
    if pk is None:
        return { 'ret_code': 1002 }

    instance = Student.objects.get(pk=pk)
    form = StudentForm(request.POST, instance=instance)
    
    if not form.is_valid():
        logger.warn("form is invalid");
        return { 'ret_code': 1002 }

    form.save()
    return { 'ret_code': 0}


@require_POST
@as_json
def delete_student(request):
    pk = request.POST.get("pk", '')
    Student.objects.filter(pk=pk).delete()
    return {'ret_code': 0}

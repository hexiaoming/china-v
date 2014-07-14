#coding: utf8
from itertools import chain

from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django import forms

import django_tables2 as tables
from django_tables2 import RequestConfig 
import django_active_tab as active_tab
from django_render_csv import as_csv

from students.models import VoteRecord


class VoteTable(tables.Table):
    class Meta:
        model = VoteRecord
        fields=("student", "datetime", "ip", "audience")
        empty_text = u'暂无投票数据'
        orderable=False
        attrs = {
            'class': 'table table-bordered table-striped'
        }


@require_GET
@active_tab('votes')
def index(request):
    votes = VoteRecord.objects.all().order_by('-pk')
    table = VoteTable(votes)
    RequestConfig(request, paginate={"per_page": 25}).configure(table)

    return render(request, "shake/backend.html", {
        "table": table
    })



@require_GET
@as_csv(filename=u'votes.csv')
def exports(request):
    votes = VoteRecord.objects.all().order_by('-datetime')
    return chain([[u'学员', u'投票时间', 'ip', u'观众']], map(lambda vote: [
        vote.student,
        vote.datetime, 
        vote.ip, 
        vote.audience
    ], votes))

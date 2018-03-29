# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime
from datetime import datetime

# Create your views here.

def index(request):
    time_dict = {
        'date': strftime("%b %m, %Y %I:%M %p")
    }
    return render(request, 'first_app/index.html', time_dict)
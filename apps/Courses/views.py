# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        'Courses': Course.objects.all()
    }
    return render(request, 'Courses/index.html', context)

def create(request):
    Course.objects.create(
        name=request.POST['Name'],
        desc=request.POST['Description'],
    )
    return redirect('/index')

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/index')
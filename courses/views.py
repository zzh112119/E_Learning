from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Course
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def course_list(request):
	courses = Course.objects.all().order_by('name')
	print('sth')
	return render(request,'courses/course_list.html',{'courses':courses})

@login_required(login_url="/accounts/login/")
def course_detail(request,id):
	course_info = Course.objects.get(id=id)
	courses = Course.objects.all().order_by('name')
	return render(request,'courses/course_detail.html',{'course':course_info,'courses':courses})

@login_required(login_url="/accounts/login/")
def course_create(request):
	if request.method == "POST":
		form = forms.CreateCourse(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('courses:index')
	else:
		form = forms.CreateCourse()
	return render(request, 'courses/course_create.html',{'form':form})
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Course, Quiz, Question, Answer
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required, teacher_required, supervisor_required
from . import forms
from django.views.generic import ListView, CreateView
from django.db.models import Avg, Count

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
@teacher_required
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


class QuizListView(ListView):
	model = Quiz
	ordering = ('name', )
	context_object_name = 'quizzes'
	template_name = 'courses/quiz_list.html'

	def get_queryset(self, id):
		course_info = Course.objects.get(id=id)
		queryset = self.request.user.quizzes \
			.select_related('course') \
			.annotate(questions_count=Count('questions',distinct=True))
		return queryset

class QuizCreateView(CreateView):
	model = Quiz
	fields = ('name', )
	template_name = 'courses/quiz_create.html'

	def form_valid(self, form, id):
		quiz = form.save(commit=False)
		quiz.owner = self.request.user
		quiz.course = Course.objects.get(id=id).name
		quiz.save()
		messages.success(self.request, 'The quiz is created successfully!')
		return redirect('teacher:quiz_change', quiz.pk)




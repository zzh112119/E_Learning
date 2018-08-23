from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
from django.contrib.auth import get_user_model
from accounts.forms import TeacherSignUpForm, StudentSignUpForm
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
User = get_user_model()

def signup_view(request):
	return render(request,'accounts/signup_choice.html')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print('going to redirect')
        user = form.save()
        login(self.request, user)
        return redirect('courses:index')

class StudentSignUpView(CreateView):
	model = User
	form_class = StudentSignUpForm
	template_name = 'accounts/signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'Student'
		return super().get_context_data(**kwargs)

	def form_valid(self,form):
		user = form.save()
		login(self.request,user)
		return redirect('courses:index')

def login_view(request):

	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login
			user = form.get_user()
			login(request, user)
			if "next" in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('courses:index')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html',{'form':form})


def logout_view(request):

	if request.method == 'POST':
		logout(request)
		return redirect('courses:index')


# def signup_view(request):

#   if request.method == 'POST':
#       form = UserCreationForm(request.POST)
#       # if form.is_valid():
#       user = form.save()
#       login(request, user)
#       #log the user in
#       return redirect('courses:index')

#   else:
#       form = UserCreationForm()
#   return render(request,'accounts/signup.html',{'form':form})
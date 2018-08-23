from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import (Teacher, Student, User)

class TeacherSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User

	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_teacher = True
		if commit:
			user.save()
			teacher = Teacher.objects.create(user=user)
		return user

class StudentSignUpForm(UserCreationForm):
	# major = forms.ModelMultipleChoiceField(
	# 	queryset=subject.objects.all(),
	# 	widget=forms.CheckboxSelectMultiple,
	# 	required=True
	# )
	
	class Meta(UserCreationForm.Meta):
		model = User

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student =True
		user.save()
		student = Student.objects.create(user=user)
		# student.major.add(*self.cleaned_data.get('interests'))
		return user


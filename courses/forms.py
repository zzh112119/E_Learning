from django import forms
from . import models

class CreateCourse(forms.ModelForm):
	"""docstring for CreateCourse"""
	class Meta:
		model = models.Course
		fields = ['name','slug','body']
		
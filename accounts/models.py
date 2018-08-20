from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_teaching_assistant = models.BooleanField(default=False)
	is_supervisor = models.BooleanField(default=False)

class Student(models.Model):
	name = models.CharField(max_length=50)
	student_id = models.IntegerField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	def __str__(self):
		return self.user.username

class Teacher(models.Model):
	name = models.CharField(max_length=50)
	teacher_id = models.IntegerField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	def __str__(self):
		return self.user.username

class Supervisor(models.Model):
	name = models.CharField(max_length=50)
	teacher_id = models.IntegerField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	def __str__(self):
		return self.user.username	

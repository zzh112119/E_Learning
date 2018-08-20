from django.db import models
# from django.contrib.auth.models import User as Auth_User
# from accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Course(models.Model):
    # fields...
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        app_label = 'courses'

    def __str__(self):
    	return self.name

    def snippet(self):
        return self.body[:50] + '...'

# class Quiz(models.Model):
#     owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="quizzes")
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="quizzes")
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="questions")
#     text = models.CharField('Question', max_length=255)

#     def __str__(self):
#         return self.text

# class Answer(models.Model):
#     question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
#     text = models.CharField('Answer', max_length=255)
#     is_correct = models.BooleanField('Correct answer',default=False)

#     def __str__(self):
#         return self.text

# class Grade(models.Model):



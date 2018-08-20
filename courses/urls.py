from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='index'),
    path('create/',views.course_create,name='create'),
    path('<int:id>',views.course_detail, name='detail'),
]
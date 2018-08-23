from django.urls import path, include

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='index'),
    path('create/',views.course_create,name='create'),
    path('<int:id>/',include(([
    	path('',views.course_detail, name='detail'),
    	path('quiz/',views.QuizListView.as_view(),name="quiz_list"),
    	path('quiz/create/',views.QuizCreateView.as_view(), name="quiz_create"),
    	# path('<int:pk>')
    	])))
]
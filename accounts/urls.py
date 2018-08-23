from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('signup/',views.signup_view,name='signup'),
	path('signup/student/',views.StudentSignUpView.as_view(),name='student_signup'),
	path('signup/teacher/',views.TeacherSignUpView.as_view(),name='teacher_signup'),
	path('login/',views.login_view,name='login'),
	path('logout/',views.logout_view,name='logout'),
    # path('', views.course_list, name='index'),
    # path('<int:id>',views.course_detail, name='detail'),
]
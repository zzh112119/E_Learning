from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('signup/',views.TeacherSignUpView.as_view(),name='signup'),
	path('login/',views.login_view,name='login'),
	path('logout/',views.logout_view,name='logout'),
    # path('', views.course_list, name='index'),
    # path('<int:id>',views.course_detail, name='detail'),
]
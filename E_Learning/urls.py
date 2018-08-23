"""projectZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic import TemplateView
from courses import views as courses_views

urlpatterns = [
    path('',courses_views.course_list),
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls, name='admin'),
    # url(r'^index/$',TemplateView.as_view(template_name='courses/example.html')),
]

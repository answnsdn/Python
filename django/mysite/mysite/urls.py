"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),
    path('name/', views.name),
    path('info/', views.introduce),
    path('raname/', views.raname),
    #str : 문자열이라는 의미
    #int : 숫자만 들어오게 하고 싶을 때 사용
    path('yourname/<str:name>/', views.yourname),
    path('exam200610/<str:name>/<int:age>',views.exam200610),
    path('multiple/<int:num1>/<int:num2>/', views.multiple),
    path('googoo/<int:big>/<int:small>/', views.googoo),
    path('dtl/', views.dtl),
    path('forif/', views.forif),
]

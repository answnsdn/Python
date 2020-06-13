# pages/urls.py
from django.urls import path
from . import views
app_name = "pages"

urlpatterns = [
    path('index/',views.index, name = "index"),
    path('lunch/<str:name>/',views.lunch, name="lunch"),
    path('throw/',views.throw,name="throw"),
    path('catch/',views.catch, name="catch"),
    path('lotto/',views.lotto, name="lotto"),
    path('getlotto/',views.getlotto,name="getlotto"),
    path('artii/',views.artii,name = "artii"),
    path('result/',views.result,name="result"),
]
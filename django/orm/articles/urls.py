from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('index/',views.index, name="index"),
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),
    path('introduce/',views.introduce, name="introduce"),
    path('<int:article_pk>/',views.detail, name="detail"),
    path('<int:article_pk>/delete/',views.delete, name="delete"),
    path('<int:article_pk>/edit/',views.edit, name="edit"),
]
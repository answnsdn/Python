from django.urls import path
from . import views

#어플리케이션 name space
app_name = "musicians"

#장고 내부적으로 정해진 이름
urlpatterns = [
    # u - v - t 순서 고정,
    # path_name을 무엇으로 지었는지,
    # 어떤 view 함수를 실행하는지
    # 하나의 경로에 하나의 view 함수
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:musician_pk>/',views.detail, name="detail"),
    path('<int:musician_pk>/update/',views.update, name="update"),
    path('<int:musician_pk>/delete/',views.delete, name="delete"),
    path('<int:musician_pk>/album_create/', views.album_create, name="album_create"),
]
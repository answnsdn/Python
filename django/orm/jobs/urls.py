from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('past_life/', views.past_life, name="past_life"),
    path('detail/', views.detail, name="detail")
]
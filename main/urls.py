from django.urls import path
from .views import RoomView
from . import views

urlpatterns = [
    path('', views.index),
    path('home', RoomView.as_view()),
]

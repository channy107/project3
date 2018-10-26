from django.contrib import admin
from django.urls import path, include
from file import views
urlpatterns = [
    path('upload1', views.upload1, name='upload1'),
    path('upload2', views.upload2, name='upload2'),
]

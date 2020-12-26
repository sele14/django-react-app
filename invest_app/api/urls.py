from django.contrib import admin
from django.urls import include, path
from . import views

# when at root, show index() route endpoint
urlpatterns = [
    path('', views.index),
]
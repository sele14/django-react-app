from django.contrib import admin
from django.urls import include, path
from .views import InvestmentsView
 
urlpatterns = [
    path('', InvestmentsView.as_view()),
]
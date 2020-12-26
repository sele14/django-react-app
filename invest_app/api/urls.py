from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
]

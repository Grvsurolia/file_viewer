# file_upload/urls.py
from django.urls import path
from . import views

app_name = 'file_app'

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from django.shortcuts import render
from django.views import generic
from .models import Post
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

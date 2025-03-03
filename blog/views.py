from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"

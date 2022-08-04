from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model =  Post
    ordering = '-pk'
    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post_page.html'


# Create your views here.

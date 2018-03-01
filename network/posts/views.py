from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = 'users:login'
    # redirect_field_name = 'user:signup'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    # redirect_field_name = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title']
    # redirect_field_name = 'users:login'

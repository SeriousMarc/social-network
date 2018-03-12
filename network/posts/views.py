from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import CreatePost
# Create your views here.
class PostListView(ListView):
    model               = Post
    login_url           = 'users:login'
    # redirect_field_name = 'user:signup'

class PostDetailView(DetailView):
    model               = Post
    # redirect_field_name = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class          = CreatePost
    template_name       = 'posts/post_create.html'
    login_url           = 'users:login'
    # fields              = ['title', 'content', 'slug', 'img']
    # redirect_field_name = 'users:login'
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance        = form.save(commit=False)
            instance.user   = request.user
            instance.save()
            return redirect('posts:list')
        return render(request, self.template_name, {'form': form})

# class PostEditView(LoginRequiredMixin, UpdateView):
#     model               = Post
#     # form_class          = CreatePost
#     template_name       = 'posts/post_edit.html'
#     login_url           = 'users:login'
#     fields              = ['title', 'content', 'img']
#     # redirect_field_name = 'posts:list'
#     # success_url         = 'posts:list'

# def post_edit_view(request, slug):
#     instance = Post.objects.get(slug=slug)
#     print(instance.title)
#     form = CreatePost(request.POST.data, request.FILES, instance=instance)
#     print(form.fields)
#     if form.is_valid():
#         form.save()
#         return redirect('posts:list')
#     return render(request, 'posts/post_edit.html', {'form': form})

@login_required(login_url="users:login")
def post_edit_view(request, slug):
    instance_1 = Post.objects.get(slug=slug)
    print(instance_1.title)
    if request.method == 'POST':
        form = CreatePost(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else: # method GET
        form = CreatePost(request.GET, instance=Post.objects.get(slug=slug))
        print(form.fields['title'])
    return render(request, 'posts/post_edit.html', {'form':form})

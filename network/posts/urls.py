from django.urls import path
from . import views
# from django.views.generic import TemplateView

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name="list"),
    path('create/', views.PostCreateView.as_view(), name="post-create"),
    path('<slug>/', views.PostDetailView.as_view(), name="detail"),
    path('<slug>/edit/', views.post_edit_view, name="post-edit"),
]

from django.urls import path
from . import views
# from django.views.generic import TemplateView

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name="list"),
    path('detail/<slug>/', views.PostDetailView.as_view(), name="detail"),
]

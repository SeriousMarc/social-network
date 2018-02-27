from django.urls import path

from .views import PostRudView, PostAPIView

app_name = 'posts.api'
urlpatterns = [
    path('', PostAPIView.as_view(), name="post-create"),
    path('<pk>/', PostRudView.as_view(), name="post-rud"),
]

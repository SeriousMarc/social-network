from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import PostRudView, PostAPIView

app_name = 'posts.api'
urlpatterns = [
    path('', PostAPIView.as_view(), name="post-create"),
    # path('auth/token/', obtain_jwt_token),
    path('<pk>/', PostRudView.as_view(), name="post-rud"),
]

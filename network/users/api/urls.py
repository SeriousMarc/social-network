from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateView, UserRetrieveUpdateView

app_name = 'users.api'
urlpatterns = [
    path('', UserCreateView.as_view(), name="user-create"),
    path('<username>', UserRetrieveUpdateView.as_view(), name="profile-rud"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

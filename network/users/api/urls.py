from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

app_name = 'users.api'
urlpatterns = [
    path('', CreateView.as_view(), name="profile-create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

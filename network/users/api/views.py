from rest_framework import generics
from .serializers import ProfileSerializer
from users.models import Profile
from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

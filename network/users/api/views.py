from rest_framework import generics
from .serializers import UserProfileSerializer
from users.models import Profile

class CreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

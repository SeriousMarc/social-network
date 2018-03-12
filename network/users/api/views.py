from rest_framework import generics
from .serializers import UserSerializer
from users.models import Profile
from django.contrib.auth.models import User

import itertools

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field        = 'username'
    serializer_class    = UserSerializer
    queryset            = User.objects.all()





# return list(itertools.chain(User.objects.all(), Profile.objects.all()))



# class ProfileCreateView(generics.CreateAPIView):
#     queryset            = Profile.objects.all()
#     serializer_class    = ProfileSerializer
#
#     def perform_create(self, serializer):
#         """Save the post data when creating a new profile"""
#         serializer.save()

from rest_framework import serializers
from users.models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'location',
            'birth_date',
        ]
        read_only_fields = ('id', 'user')

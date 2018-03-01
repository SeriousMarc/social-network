from django.contrib.auth.models import User
# from django.db.models.fields import EmailField
from rest_framework import serializers
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
        Extending ProfileSerializer with User model fields
    """
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'bio',
            'location',
            'birth_date',
        ]
        read_only_fields = ('id', 'user')

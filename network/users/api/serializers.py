from django.contrib.auth.models import User
# from django.db.models.fields import EmailField
from rest_framework import serializers
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
        Extending ProfileSerializer with User model fields
    """
    first_name  = serializers.CharField(source='user.first_name')
    last_name   = serializers.CharField(source='user.last_name')
    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'bio',
            'location',
            'birth_date',
        ]
        read_only_fields = ('id', 'user')

class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            # 'profile',
        ]
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

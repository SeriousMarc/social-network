from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'title',
            'slug',
            'content',
            'pub_date',
        ]
        read_only_fields = ['user']

    def validate_title(self, value):
        qs = Post.objects.filter(title__iexact=value)
        # wtf is this for?
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used.")
        return value

from django.db.models import Q
from rest_framework import generics, mixins
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from posts.models import Post

class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'
    serializer_class    = PostSerializer
    # permission_classes = []
    # queryset = Post.objects.all()

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query))
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'pk'
    serializer_class    = PostSerializer
    permission_classes  = [IsOwnerOrReadOnly]
    # queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

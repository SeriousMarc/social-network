from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField()
    content     = models.TextField()
    img         = models.ImageField(blank=True)
    pub_date    = models.DateTimeField(auto_now_add=True)
    users_like  = models.ManyToManyField(User, blank=True, related_name='post_liked')

    def __str__(self):
        return self.title




# class Like(models.Model):
#     posts   = models.ManyToManyField(Post, through='Likes')
#     created = models.BooleanField(default=False)
#
# class Likes(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
#     like = models.ForeignKey(Like, on_delete=models.CASCADE, default=None)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

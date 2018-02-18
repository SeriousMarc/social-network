from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField()
    img = models.ImageField(blank=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

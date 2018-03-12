from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    bio         = models.TextField(max_length=500, blank=True, null=True)
    location    = models.CharField(max_length=30, blank=True, null=True)
    birth_date  = models.DateField(null=True, blank=True)
    avatar      = models.ImageField(default="media/default-avatar.png", blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile = Profile.objects.create(user=instance)

    # @property
    # def user_data(self):
    #     return {
    #         'first_name':self.user.first_name,
    #         'last_name':self.user.last_name,
    #         'email':self.user.email
    #     }

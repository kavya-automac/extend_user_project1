from django.db import models
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=50)
    location=models.CharField(max_length=50)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

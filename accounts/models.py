from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[validate_email])
    profile_image = models.ImageField(upload_to='accounts/profile_images/', default='accounts/profile_images/user.png', blank=True, null=True)

    def __str__(self):
        return self.user.username

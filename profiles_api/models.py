from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Model definition for Profile."""
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=250,blank=True)
    city=models.CharField(max_length=100,blank=True)
    avatar=models.ImageField(null=True,blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username



class ProfileStatus(models.Model):
    """Model definition for ProfileStatus."""
    user_profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    status_content=models.CharField(max_length=240)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for ProfileStatus."""

        verbose_name = 'status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return str(self.user_profile)


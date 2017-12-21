from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)

    class Meta:
        #ordering = ['-name ']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.name

    @property
    def name(self):
        return 'profile-'+str(self.id)


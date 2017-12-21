from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class S3File(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(None))
    filename = models.CharField(max_length=255, blank=False)
    filetype = models.CharField(max_length=255, blank=True)
    s3_filename = models.CharField(max_length=512, blank=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ['-name ']
        verbose_name = 'S3 File'
        verbose_name_plural = 'S3 Files'

    def __str__(self):
        return self.filename

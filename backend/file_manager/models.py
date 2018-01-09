from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    filename = models.CharField(max_length=255, blank=False)
    filetype = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.SET(None))
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ['-name ']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.filename

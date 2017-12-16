from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.text import slugify

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='DeletedUser')[0]

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body_raw = models.TextField()
    body_html = models.TextField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    is_published = models.BooleanField(default=False)
    # thumbnail
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
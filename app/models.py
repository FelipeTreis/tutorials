from django.contrib.auth.models import User
from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
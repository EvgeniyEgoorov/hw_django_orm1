from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, default=None)
    image = models.URLField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(max_length=150, default=None)

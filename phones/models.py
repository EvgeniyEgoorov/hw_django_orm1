from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150)

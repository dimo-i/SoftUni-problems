from django.db import models


# Create your models here.

class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    ING_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image_url = models.URLField()

    ingredients = models.CharField(
        max_length=ING_MAX_LENGTH
    )

    description = models.TextField()

    time = models.IntegerField()


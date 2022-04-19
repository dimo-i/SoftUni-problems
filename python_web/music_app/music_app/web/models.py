from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from django import forms

from music_app.web.validators import validate_letters


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_letters,
        ),

    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )

    )


class Album(models.Model):
    ALBUM_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30

    GENRE_MAX_LENGTH = 30
    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),

    ]

    PRICE_MIN_VALUE = 0

    album_name = models.CharField(
        max_length=ALBUM_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRE_CHOICES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators = (
            MinValueValidator(PRICE_MIN_VALUE),
        )

    )

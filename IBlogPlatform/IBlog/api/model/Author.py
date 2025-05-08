from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from pathlib import Path
# Import your validators
from .validators import noSpaces_noSpecial_validator, XSS_validator


# Assuming you have a default image in your media folder
DEFAULT_PERSONAL_IMAGE = 'images/default_personal.png'
DEFAULT_WALLPAPER_IMAGE = 'images/default_wallpaper.png'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    authName = models.CharField(
        max_length=100, unique=True, validators=[noSpaces_noSpecial_validator])
    authEmail = models.EmailField(unique=True)
    authImg = models.ImageField(upload_to='images/%Y/%m/%d/personal/',
                                default=DEFAULT_PERSONAL_IMAGE, null=True, blank=True)
    authWallpaper = models.ImageField(
        upload_to='images/%Y/%m/%d/wallpaper/', default=DEFAULT_WALLPAPER_IMAGE, null=True, blank=True)
    authBirthDate = models.DateField()
    authBio = models.TextField(validators=[XSS_validator])
    authCreatedAt = models.DateTimeField(auto_now_add=True)
    authUpdatedAt = models.DateTimeField(auto_now=True)
    authPassword = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    @property
    def age(self):
        now = timezone.now()  # This will automatically be in the project's timezone
        return now.year - self.authBirthDate.year - ((now.month, now.day) < (self.authBirthDate.month, self.authBirthDate.day))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.authName

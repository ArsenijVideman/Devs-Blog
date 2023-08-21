from typing import Any
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CHOICES = (('male', 'MALE'), ('female', 'FEMALE'), ('none', 'NONE'),)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        'User Image', default='user_images/default_user.png', upload_to='user_images')
    gender = models.CharField(max_length=6, choices=CHOICES, default='male')
    agreement = models.BooleanField(
        default=False,
        verbose_name='Consent to send email notifications')

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 and image.width > 256:
            SIZE = (256, 256)
            image.thumbnail(SIZE)
            image.save(self.img.path)

    def __str__(self):
        return f'User Profile {self.user.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

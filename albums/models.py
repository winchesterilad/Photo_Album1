from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Album(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='photos'
    )

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='photos/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
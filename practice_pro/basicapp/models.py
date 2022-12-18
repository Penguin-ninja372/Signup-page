from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse("index")

    def __str__(self):
        return self.username
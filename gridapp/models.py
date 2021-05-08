from django.db import models

# Create your models here.

class Gallery(models.Model):
  title = models.CharField()
  image = models.ImageField()

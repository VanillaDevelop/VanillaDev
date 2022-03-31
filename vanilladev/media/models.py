from django.db import models

# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to='images')
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
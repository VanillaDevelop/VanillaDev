from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField
from django.db.models import ManyToManyField

# Create your models here.
class Category(models.Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    content = RichTextField()
    categories = ManyToManyField(Category)


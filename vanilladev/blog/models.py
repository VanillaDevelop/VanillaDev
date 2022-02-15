from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    content = RichTextField()
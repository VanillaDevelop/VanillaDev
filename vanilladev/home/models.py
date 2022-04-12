from django.db import models

class RecentProject(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField()
    link = models.CharField(max_length=128)


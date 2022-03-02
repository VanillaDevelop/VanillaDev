from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField, TextField

class Project(models.Model):
    title = CharField(max_length=255)
    created_at = models.DateField()
    motivation_summary = TextField()
    project_summary = TextField()
    dataset_url = models.CharField(max_length=255, blank=True)
    repository_url = models.CharField(max_length=255, blank=True)
    download_link_url = models.CharField(max_length=255, blank=True)
    project_page_url = models.CharField(max_length=255, blank=True)
    technology_stack_csv = models.CharField(max_length=255, blank=True)
    project_idea = RichTextField()
    technology_stack = RichTextField()
    functionality = RichTextField()
    lessons_learned = RichTextField()
    is_published = models.BooleanField()
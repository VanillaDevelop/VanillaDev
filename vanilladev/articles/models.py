from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField, TextField

class Article(models.Model):
    title = CharField(max_length=255)
    created_at = models.DateField()
    motivation_summary = TextField()
    article_summary = TextField()
    results_summary = TextField()
    dataset_url = models.CharField(max_length=255, blank=True)
    repository_url = models.CharField(max_length=255, blank=True)
    download_link_url = models.CharField(max_length=255, blank=True)
    project_page_url = models.CharField(max_length=255, blank=True)
    tools_csv = models.CharField(max_length=255, blank=True)
    article_premise = RichTextField()
    article_text = RichTextField()
    is_published = models.BooleanField()
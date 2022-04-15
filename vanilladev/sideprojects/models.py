from django.db import models
from django.utils.translation import gettext_lazy as _

class SideProject(models.Model):
    class ProjectType(models.TextChoices):
        PROFESSIONAL = 'PR', _('Professional')
        SIDEPROJECT = 'SP', _('Side Project')
        TREASURETROVE = 'TR', _('Treasure Trove')

    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=128)
    summary = models.TextField()
    technologies = models.TextField()
    notable = models.TextField()
    project_type = models.CharField(
        max_length=2,
        choices=ProjectType.choices,
        default=ProjectType.SIDEPROJECT,
    )


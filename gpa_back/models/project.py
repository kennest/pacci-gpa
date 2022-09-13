from django.core.files.storage import FileSystemStorage
from simple_history.models import HistoricalRecords
from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteModel
from django.contrib.contenttypes.fields import GenericRelation
from gpa_back.models import Document
fs = FileSystemStorage(location=str(settings.BASE_DIR) +
                       '/media/documents/')


class Project(SafeDeleteModel):
    label = models.CharField(max_length=255, blank=True, null=True)
    documents = GenericRelation(Document)
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'projects'
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
        ordering = ['label']

    def __str__(self):
        return f"{self.label}"

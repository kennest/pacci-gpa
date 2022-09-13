from simple_history.models import HistoricalRecords
from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteModel


class InterventionType(SafeDeleteModel):
    label = models.CharField("Nom type d'intervention",
                             max_length=255, null=True)
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'intervention_types'
        verbose_name = 'Type d\'Intervention'
        verbose_name_plural = 'Types d\'Interventions'
        ordering = ['label']

    def __str__(self):
        return f"{self.label}"

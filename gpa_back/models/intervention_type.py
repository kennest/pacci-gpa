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

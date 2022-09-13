
from simple_history.models import HistoricalRecords

from django.db import models
from safedelete.models import SafeDeleteModel


class Car(SafeDeleteModel):
    manufacturer = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Marque / Fabriquant")
    serial_number = models.CharField(
        max_length=255, verbose_name="Numéro Matricule")
    type = models.CharField(max_length=255, verbose_name="Type du véhicule")
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)
    history = HistoricalRecords()

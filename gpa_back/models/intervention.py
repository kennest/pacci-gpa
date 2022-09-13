
from simple_history.models import HistoricalRecords
from django.conf import settings
from safedelete.models import SafeDeleteModel
from django.contrib.contenttypes.fields import GenericRelation
from .user_profil import UserProfil
from .intervention_type import InterventionType
from .car import Car
from .document import Document
from .project import Project
from django.db import models


class Intervention(SafeDeleteModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="Projet de l'intervention", blank=True, null=True)
    applicant = models.ForeignKey(
        UserProfil, on_delete=models.CASCADE, verbose_name="Demandeur de l'intervention")
    car_concerned = models.ForeignKey(
        Car, on_delete=models.CASCADE, verbose_name="véhicule concerné par l'intervention")
    type = models.OneToOneField(
        InterventionType, verbose_name="Type de l'intervention", on_delete=models.CASCADE)
    date = models.DateField(max_length=255)
    document = GenericRelation(Document)
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)
    history = HistoricalRecords()

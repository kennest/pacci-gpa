
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
    STATUS = (
        ('APPROUVED', 'approuvé'),
        ('REFUSED', 'refusé'),
        ('PENDING', 'en attente'),
    )
    status = models.CharField(max_length=15, choices=STATUS,blank=True,null=True,default="PENDING")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="Projet de l'intervention", blank=True, null=True)
    applicant = models.ForeignKey(
        UserProfil, on_delete=models.CASCADE, verbose_name="Demandeur de l'intervention")
    car_concerned = models.ForeignKey(
        Car, on_delete=models.CASCADE, verbose_name="véhicule concerné par l'intervention")
    type = models.ForeignKey(
        InterventionType, verbose_name="Type de l'intervention", on_delete=models.CASCADE)
    date = models.DateField(max_length=255)
    document = GenericRelation(Document)
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'interventions'
        verbose_name = 'Intervention'
        verbose_name_plural = 'Interventions'
        ordering = ['project', 'type']
        unique_together = ['status', 'car_concerned','applicant']

    def __str__(self):
        return "{} | {}".format(self.type, self.project)

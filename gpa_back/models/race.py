from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from .project import Project
from .car import Car
from .user_profil import UserProfil
from .document import Document


class Race(SafeDeleteModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="Projet de la course", blank=True, null=True)
    applicant = models.ForeignKey(
        UserProfil, on_delete=models.CASCADE, verbose_name="Demandeur de la course", related_name="RaceApplicant")
    steed = models.ForeignKey(
        UserProfil, on_delete=models.CASCADE, verbose_name="Coursier exécutant la course", related_name="RaceSteed")
    car_concerned = models.ForeignKey(
        Car, on_delete=models.CASCADE, verbose_name="véhicule concerné")
    begin_date = models.DateField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.DateField(max_length=255, blank=True, null=True)
    document = GenericRelation(Document)
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'races'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['project', 'car_concerned', 'applicant']

    def __str__(self):
        return f"{self.project} | {self.car_concerned}"
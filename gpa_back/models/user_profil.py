
from simple_history.models import HistoricalRecords
from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteModel
from django.contrib.contenttypes.fields import GenericRelation
from .document import Document
from django.contrib.auth.models import User


class UserRole(SafeDeleteModel):
    label = models.CharField("Role", max_length=255, blank=True)
    history = HistoricalRecords()


class UserProfil(SafeDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documents = GenericRelation(Document)
    history = HistoricalRecords()
    role = models.ForeignKey(
        UserRole, verbose_name="Role de l'utilisateur", on_delete=models.CASCADE)

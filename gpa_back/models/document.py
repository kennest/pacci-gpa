from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from safedelete.models import SafeDeleteModel
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=str(settings.BASE_DIR) +
                       '/media/documents/')

 
class Document(SafeDeleteModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,related_name="documents_contenttype")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    published = models.DateTimeField("Crée le", auto_now_add=True)
    updated = models.DateTimeField("Crée le", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

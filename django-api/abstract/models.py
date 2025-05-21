from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class AbrstractManager(models.Manager):
    def get_object_by_public_id(self,public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ValueError, TypeError, ObjectDoesNotExist):
            raise Http404
        
# Create your models here.
class AbrstractModel(models.Model):
    public_id = models.UUIDField(db_index=True,default=uuid.uuid4,unique=True,editable=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
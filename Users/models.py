from django.db import models
from django_mongodb_backend.fields import EmbeddedModelField, ArrayField
from django_mongodb_backend.models import EmbeddedModel

# Create your models here.
from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField  # Importa el campo correcto


class Users(models.Model):
    id = ObjectIdAutoField(primary_key=True)  # Usa este tipo de ID en MongoDB
    nombre = models.CharField(max_length=100)
    nickName = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre


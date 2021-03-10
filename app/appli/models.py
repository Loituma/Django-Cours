from django.db import models
from django.utils import timezone

# Create your models here.
class Kube(models.Model):
    Nom = models.CharField(max_length=150)
    Description = models.CharField(max_length=22)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,verbose_name="Date de parution")


class Contact(models.Model):
    nom = models.CharField(max_length=150)
    mail = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    contenu = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
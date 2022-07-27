from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Utilisateur(User):
    phone = models.CharField(max_length=10, verbose_name="Téléphone")
    bucque = models.CharField(blank=True, max_length=200)
    fams = models.CharField(blank=True, max_length=200, verbose_name="Fam's")
    entreprise = models.CharField(blank=True, max_length=200, verbose_name="L'entreprise où je travaille")
    poste = models.CharField(blank=True, max_length=200, verbose_name="Mon poste")

    def __unicode__(self):
        return self.username
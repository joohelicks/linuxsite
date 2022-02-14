from django.db import models

# Create your models here.

class Distro(models.Model):
    nimi = models.CharField(max_length=50)
    kuvaus = models.TextField(max_length=2500)
    kuva = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nimi

class Artikkeli(models.Model):
    otsikko = models.CharField(max_length=50)
    teksti = models.TextField(max_length=5000)
    kuva = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.otsikko

class Postaus(models.Model):
    nimi = models.CharField(max_length=50)
    postaus = models.TextField(max_length=250)
    päivämäärä = models.DateTimeField()
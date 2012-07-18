from django.db import models

from locations.models import *


class Status(models.Model):
    pais = models.ForeignKey(Country)
    cidade = models.ForeignKey(Municipality, blank=True, null=True)
    estado = models.ForeignKey(State, blank=True, null=True)
    agencia = models.CharField(max_length=128, blank=True)
    situacao = models.CharField(max_length=128)
    observacao = models.CharField(max_length=128, blank=True)
    atualizacao = models.DateTimeField()


class Encomenda(models.Model):
    identificador = models.CharField(max_length=64, unique=True)
    status = models.ManyToManyField(Status)

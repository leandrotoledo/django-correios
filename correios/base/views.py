from datetime import datetime

from django.core import serializers
from django.utils import simplejson

from correios import Correios
from locations.models import Country, Municipality, State
from models import Status, Encomenda


def get(request, identificador):
    try:
        encomenda = Encomenda.objects.get(identificador=identificador)
    except Encomenda.DoesNotExist:
        encomenda = Correios.get_encomenda(identificador)
        [Status(
            pais = Country.objects.get(name__iexact=status.pais),
            cidade = Municipality.objects.get(name__iexact=status.cidade) or None,
            estado = State.objects.get(name__iexact=status.estado) or None,
            agencia = status.agencia or None,
            situacao = status.situacao,
            observacao = status.observacao or None,
            atualizacao = status.atualizacao
        ) for status in encomenda.status]


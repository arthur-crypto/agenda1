from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criação = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

        def __init__(self):
            return self.titulo

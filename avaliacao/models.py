from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from usuario.models import Usuario
import empresa...

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj
    enderço
    telefpne

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(6)])

    class Meta:
        unique_together = ['empresa', 'usuario']

    def __str__(self):
        return f"Avaliação de {self.empresa} por {self.usuario}"

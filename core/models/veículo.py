from django.db import models

from .modelo import Modelo
from .Acessório import Acessorio
from .cor import Cor


class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(self):
        return f"{self.id} - {self.modelo} {self.cor} {self.ano}"

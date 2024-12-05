from django.db import models
from datetime import date

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_criacao = models.DateField(default=date.today)
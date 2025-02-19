from django.db import models
from datetime import date
import os

# Create your models here.

def imagem_produto_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.codigo}.{ext}"
    return os.path.join('produtos', filename)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_criacao = models.DateField(default=date.today)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, blank=True)
    categorias = models.ManyToManyField(Categoria, blank=True, related_name='produtos')
    imagem = models.ImageField(upload_to=imagem_produto_path, default='produtos/default.webp', blank=True, null=True)

    def __str__(self):
        return self.nome
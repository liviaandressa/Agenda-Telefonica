from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
  
 
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True) 
    teleone = models.CharField(max_length=15)
    email = models.CharField(max_length=100, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao =  models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

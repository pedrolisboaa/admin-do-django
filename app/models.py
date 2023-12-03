from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=256)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tecnologia = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo
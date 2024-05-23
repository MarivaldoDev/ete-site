from django.db import models

# Create your models here.

class Menu(models.Model):
    descricao = models.CharField(max_length=100)


class Eventos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='images/')


class Calendario(models.Model):
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='docs/')


class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    perfil = models.TextField()
    mercado = models.TextField()
    imagem = models.ImageField(upload_to='images/')
from django.db import models

class Discente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    numero = models.CharField(max_length=12)
    ano = models.IntegerField()
    curso = models.CharField(max_length=50)

    def __str__(self):
        return self.id + " - " + self.nome

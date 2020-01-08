from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    generos = (
        ('F','Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Não Binário'),
        ('T', 'Trans'),
    )

    genero = models.CharField(choices=generos, max_length=3)
    endereco= models.CharField(max_length=30)



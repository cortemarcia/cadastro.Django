from django.db import models
from professores.models import Professor

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
    # relação entre professor e aluno-->
    #ForeignKey é uma chave que é perseguida, ou seja, o aluno indentifica um professor pela
    #chave primaria dele, que logo se torna uma ForeignKeypara o aluno.relação de n/1
    professor= models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
    
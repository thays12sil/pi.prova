# Create your models here.
from django.db import models

class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    vagas = models.IntegerField()
    inscritos = models.IntegerField()
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cursos/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome    
    


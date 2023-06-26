from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=9, default="#FFFFFF")

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.CharField(max_length=250)
    status = models.ForeignKey(
        to="tarefas.Status", 
        related_name="tarefas", 
        on_delete=models.PROTECT
    )
    categorias = models.ManyToManyField(
        to="tarefas.Categoria",
        related_name="tarefas"
    )
    projeto = models.ForeignKey(
        to="projetos.Projeto",
        related_name="tarefas",
        on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        to=User,
        related_name="tarefas", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo

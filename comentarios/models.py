from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    texto = models.CharField(max_length=150)
    tarefa = models.ForeignKey(
        to="tarefas.Tarefa",
        related_name="comentarios", 
        on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        to=User,
        related_name="comentarios", 
        on_delete=models.CASCADE
    )

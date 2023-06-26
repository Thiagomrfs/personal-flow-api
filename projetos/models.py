from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    criador = models.ForeignKey(
        to=User,
        related_name="projetos_criados", 
        on_delete=models.CASCADE
    )
    participantes = models.ManyToManyField(
        to=User,
        related_name="projetos_colaborados",
        blank=True
    )

    def __str__(self):
        return self.nome

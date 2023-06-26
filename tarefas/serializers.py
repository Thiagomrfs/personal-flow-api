from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id", "nome", "cor")

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id", "nome")

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = "__all__"

class TaskCommentSerializer(serializers.Serializer):
    titulo = serializers.CharField(read_only=True)
    texto = serializers.CharField(read_only=True)
    autor = serializers.SlugRelatedField(slug_field="username", read_only=True)
from rest_framework import serializers
from .models import Projeto
from tarefas.models import Tarefa
from tarefas.serializers import StatusSerializer, CategoriaSerializer

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
    descricao = serializers.CharField()

class DetailedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = (
            "id", "nome", "descricao", 
            "participantes", "criador"
        )

class TarefaOnProjectSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    categorias = CategoriaSerializer(read_only=True, many=True)
    autor = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Tarefa
        fields = (
            "id", "titulo", "data_inicio", 
            "data_fim", "descricao", "status", "categorias",
            "autor"
        )
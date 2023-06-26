from rest_framework.views import APIView, Response, status
from rest_framework import generics

from projetos.models import Projeto

from .serializers import ProjectSerializer, TarefaOnProjectSerializer, DetailedProjectSerializer
from tarefas.serializers import TarefaSerializer

class ViewProjects(APIView):
    def get(self, request):
        user = request.user

        criados = user.projetos_criados.all()
        colaborados = user.projetos_colaborados.all()
        qs = criados.union(colaborados)

        serializer = ProjectSerializer(qs, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        user = request.user

        try:
            instance = Projeto(
                nome = request.data["nome"],
                descricao = request.data["descricao"],
                criador = user
            )
            instance.save()
            instance.participantes.add(user)
        except:
            return Response({"message": "não foi possível criar o projeto!"})

        return Response(status=status.HTTP_201_CREATED)

class ViewProject(generics.RetrieveDestroyAPIView):
    queryset = Projeto.objects.all()
    serializer_class = DetailedProjectSerializer

    def patch(self, request, pk):
        instance = Projeto.objects.get(pk=pk)
        serializer = DetailedProjectSerializer(
            instance, data=request.data, 
            partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewProjectTasks(APIView):
    def get(self, request, pk):
        try: 
            projeto = Projeto.objects.get(pk=pk)
        except:
            return Response(
                {"message": "Projeto não encontrado"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        qs = projeto.tarefas.all()
        serializer = TarefaOnProjectSerializer(qs, many=True)

        return Response(serializer.data)
    
    def post(self, request, pk):
        serializer = TarefaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


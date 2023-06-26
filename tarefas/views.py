from rest_framework import generics
from rest_framework.views import APIView, Response, status
from .models import *
from .serializers import *
from comentarios.models import Comentario

class ListCategories(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ListStatuses(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ViewTask(generics.RetrieveDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def patch(self, request, pk):
        instance = Tarefa.objects.get(pk=pk)
        serializer = TarefaSerializer(
            instance, data=request.data, 
            partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewTaskComments(APIView):
    def get(self, request, pk):
        try: 
            task = Tarefa.objects.get(pk=pk)
        except:
            return Response(
                {"message": "Tarefa não encontrada"},
                status=status.HTTP_400_BAD_REQUEST
            )

        qs = task.comentarios.all().order_by("-id")

        serializer = TaskCommentSerializer(qs, many=True)

        return Response(serializer.data)
    
    def post(self, request, pk):
        user = request.user

        try: 
            task = Tarefa.objects.get(pk=pk)
        except:
            return Response(
                {"message": "Tarefa não encontrada"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            instance = Comentario(
                texto = request.data["texto"],
                tarefa = task,
                autor = user
            )
            instance.save()
        except:
            return Response({"message": "não foi possível criar o comentario!"})

        return Response(status=status.HTTP_201_CREATED)
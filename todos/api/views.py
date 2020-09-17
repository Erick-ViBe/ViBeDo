from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from todos.models import Todo
from todos.api.serializers import TodoSerializer
from todos.api.permissions import IsAuthorOrNot


class TodoCreateAPIView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [ IsAuthenticated ]


    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class TodoListAPIView(generics.ListAPIView):
    serializer_class = TodoSerializer


    def get_queryset(self):
        queryset = Todo.objects.filter(author=self.request.user.pk)

        return queryset

    permission_classes = [ IsAuthenticated ]


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [ IsAuthenticated, IsAuthorOrNot ]


class TodoChangeDoneStateAPIView(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.done = not todo.done
        todo.save()

        context = {
            'message' : 'Succesfully done state change'
        }

        return Response(data=context, status=status.HTTP_200_OK)

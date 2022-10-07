from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.serializers import TodoSerializer
from todoapp.models import Todos
from rest_framework import  authentication,permissions


class TodosView(ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)


    def create(self, request, *args, **kwargs):
        serializer=TodoSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    # def list(self, request, *args, **kwargs):
    #     todos=Todos.objects.filter(user=request.user)
    #     serializer=TodoSerializer(todos,many=True)
    #     return Response(data=serializer.data)


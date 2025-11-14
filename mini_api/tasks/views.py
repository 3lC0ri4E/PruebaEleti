from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Cada usuario solo ve sus propias tareas
        return Task.objects.filter(usuario=self.request.user).order_by('-fecha_de_creacion')
    
    def perform_create(self, serializer):
        # Asignar automáticamente el usuario actual al crear una tarea
        serializer.save(usuario=self.request.user)
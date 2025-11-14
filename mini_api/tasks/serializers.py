from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'nombre', 'completada', 'fecha_de_creacion', 'usuario']
        read_only_fields = ['id', 'fecha_de_creacion', 'usuario']
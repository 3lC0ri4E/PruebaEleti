from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_de_creacion']
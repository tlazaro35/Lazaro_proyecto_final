from django.db import models

# Create your models here.

class Usuario(models.Model) :
    Usuario = models.CharField(max_length=100)
    Contraseña = models.CharField(max_length=100)
    Trabajo = models.CharField(max_length=500)
    Email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.Usuario
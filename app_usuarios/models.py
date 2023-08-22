from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, Usuario, Contraseña=None, **extra_fields):
        if not Usuario:
            raise ValueError('El campo Usuario debe estar configurado')
        user = self.model(Usuario=Usuario, **extra_fields)
        user.set_password(Contraseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, Usuario, Contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(Usuario, Contraseña, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    Usuario = models.CharField(max_length=100, unique=True)
    Contraseña = models.CharField(max_length=100)
    Trabajo = models.CharField(max_length=500)
    Email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'Usuario'
    REQUIRED_FIELDS = ['Email']

    def __str__(self):
        return self.Usuario
    

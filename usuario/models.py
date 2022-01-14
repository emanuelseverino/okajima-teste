from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        usuario = self.model(email=email, username=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff precisa ter is_staff=True')
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    codigorca = models.CharField(max_length=5, unique=True)
    nomerca = models.CharField(max_length=100, blank=True, null=True)
    codigosv = models.CharField(max_length=100, blank=True, null=True)
    nomesv = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    faixa = models.CharField(max_length=100, blank=True, null=True)
    funcao = models.CharField(max_length=100, blank=True, null=True)

    is_staff = models.BooleanField('Membro da Equipe',default=False)

    USERNAME_FIELD = 'codigorca'
    REQUIRED_FIELDS = ['first_name', 'last_name','username',]

    def __str__(self):
        return self.email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('E-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo', Usuario.ADMIN)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    CANDIDATO = 'candidato'
    EMPRESA = 'empresa'
    ADMIN = 'admin'
    TIPO_CHOICES = [
        (CANDIDATO, 'Candidato'),
        (EMPRESA, 'Empresa'),
        (ADMIN, 'Administrador'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=CANDIDATO)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email

    @property
    def is_candidato(self):
        return self.tipo == self.CANDIDATO

    @property
    def is_empresa(self):
        return self.tipo == self.EMPRESA


class TokenRedefinicaoSenha(models.Model):
    CANAL_EMAIL = 'email'
    CANAL_WHATSAPP = 'whatsapp'
    CANAL_CHOICES = [
        (CANAL_EMAIL, 'E-mail'),
        (CANAL_WHATSAPP, 'WhatsApp'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tokens_senha')
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    canal = models.CharField(max_length=10, choices=CANAL_CHOICES, default=CANAL_EMAIL)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Token de Redefinição de Senha'
        verbose_name_plural = 'Tokens de Redefinição de Senha'

    def esta_valido(self):
        from django.utils import timezone
        from datetime import timedelta
        return not self.usado and (timezone.now() - self.criado_em) < timedelta(hours=2)

    def __str__(self):
        return f'Token de {self.usuario.email} ({self.canal})'

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User


class RegisteredUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('O nome de usuário é obrigatório')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class RegisteredUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = 'username'

    objects = RegisteredUserManager() 

    def _str_(self):
        return self.username 

class Produto(models.Model):
    loja = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=1000, default='Sem descrição')

    def __str__(self):
        return f"{self.loja} - {self.descricao}"

class Category(models.Model):
    name = models.CharField(max_length=100)

class ClothingItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Produto1(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

class Compra(models.Model):
    usuario = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.quantidade}x {self.produto.descricao} por {self.usuario.username} em {self.data_compra}"


class Item(models.Model):
    TIPOS_PRODUTO = (
        ('calca', 'Calça'),
        ('bermuda', 'Bermuda'),
        ('camisa', 'Camisa'),
        ('tenis', 'Tênis'),
        ('acessorio', 'Acessório'),
    )
    TIPOS_TAMANHO = (
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo_produto = models.CharField(max_length=20, choices=TIPOS_PRODUTO)
    tamanho = models.CharField(max_length=5, choices=TIPOS_TAMANHO, null=True, blank=True)
    condicao = models.CharField(max_length=20)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='items', null=True, blank=True)

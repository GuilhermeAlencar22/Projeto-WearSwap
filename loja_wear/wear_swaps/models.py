from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings

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

class RegisteredUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_set',
        related_query_name='user',
    )

    USERNAME_FIELD = 'username'

    objects = RegisteredUserManager()

    def __str__(self):
        return self.username

class Produto(models.Model):
    loja = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=1000, default='Sem descrição')
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return f"{self.loja} - {self.descricao}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ClothingItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

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
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    foto = models.ImageField(upload_to='items', null=True, blank=True)

class LojaItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='item_images')

    def __str__(self):
        return self.nome

class ItemAdicionado(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='item_images')

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class ItemCarrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Define o valor padrão como 1
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.descricao} - {self.quantidade} unidade(s)"

class Denuncia(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.motivo
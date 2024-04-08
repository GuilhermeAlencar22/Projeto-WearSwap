from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class RegisteredUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('O nome de usuário é obrigatório')

        user = self.model(
            username=username,
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class RegisteredUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)

    objects = RegisteredUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    


class Produto(models.Model):
   loja = models.CharField(max_length=100)
   categoria = models.CharField(max_length=100)
   estado = models.CharField(max_length=100)
   preco = models.DecimalField(max_digits=10, decimal_places=2)
   descricao = models.CharField(max_length=1000, default='Sem descrição')


  
   def __str__(self):
       return f"Nome da loja: {self.loja} - Nome completo: {self.descricao} - Nicho: {self.categoria} - Telefone: {self.estado} - Idade:{self.preco}"
   



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
    # Adicione outros campos conforme necessário




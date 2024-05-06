from django.urls import path
from . import views
from django.contrib import admin
from .views import delete_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'), 
    path('homepage/', views.homepage, name='homepage'), 
    path('register/', views.register_view, name='register'),
    path('ver_produto/', views.ver_produto, name="ver_produto" ),
    path('produto_inserido/<int:produto_id>/', views.produto_inserido, name='produto_inserido'),
    path('ver_loja_criada/<int:produto_id>/', views.ver_loja_criada, name='ver_loja_criada'),
    path('filtro/', views.filtro, name='filtro'),
    path('configuracoes/', views.configuracoes_view, name='configuracoes'),
    path('alterar_senha/', views.alterar_senha_view, name='alterar_senha'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('account_deleted/', views.account_deleted, name='account_deleted'),
]
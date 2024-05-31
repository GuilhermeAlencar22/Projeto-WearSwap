from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views
from .views import delete_account, ver_item, ver_loja_criada, ver_carrinho

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
    path('ver_item/<int:produto_id>/', views.ver_item, name='ver_item'),
    path('ajuda/', views.ajuda_view, name='ajuda'),
    path('item/inserir/<int:produto_id>/', views.item_inserido, name='item_inserido'),
    path('itens/<int:produto_id>/', views.itens_adicionados, name='itens_adicionados'),
    path('carrinho/', views.ver_carrinho, name='carrinho'),
    path('adicionar_ao_carrinho/<int:item_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('remover_do_carrinho/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

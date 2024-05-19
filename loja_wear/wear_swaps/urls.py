from django.urls import path
from . import views
from django.contrib import admin
from .views import delete_account
from .views import ver_item
from django.conf import settings
from django.conf.urls.static import static
from .views import ver_loja_criada


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
    # path('apagar_item/<int:item_id>/', views.apagar_item, name='apagar_item')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
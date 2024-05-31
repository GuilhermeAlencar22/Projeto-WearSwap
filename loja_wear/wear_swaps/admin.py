from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RegisteredUser, Produto, Category, ClothingItem, Compra, Item, LojaItem, ItemAdicionado, ItemCarrinho

class RegisteredUserAdmin(UserAdmin):
    model = RegisteredUser
    list_display = ['username', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ()}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['loja', 'descricao', 'categoria', 'estado', 'preco']
    search_fields = ['loja', 'descricao']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['produto', 'tipo_produto', 'tamanho', 'condicao', 'descricao', 'preco']
    search_fields = ['produto__loja', 'descricao']

admin.site.register(RegisteredUser, RegisteredUserAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Category)
admin.site.register(ClothingItem)
admin.site.register(Compra)
admin.site.register(Item, ItemAdmin)
admin.site.register(LojaItem)
admin.site.register(ItemAdicionado)
admin.site.register(ItemCarrinho)

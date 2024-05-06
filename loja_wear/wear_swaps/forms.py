from django import forms
from .models import Item

class ProdutoForm(forms.Form):
    loja = forms.CharField(label='Nome da loja', max_length=100)
    categoria = forms.CharField(label='Categoria do produto', max_length=100)
    estado = forms.CharField(label='Estado do produto', max_length=100)
    preco = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2)
    descricao = forms.CharField(label='Descrição do produto', max_length=100)




class SearchForm(forms.Form):
    keyword = forms.CharField(label='Palavra-chave', max_length=100)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['tipo_produto', 'tamanho', 'condicao', 'descricao', 'foto', 'preco']  # Inclua o campo 'preco'
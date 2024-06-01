from django import forms
from .models import Produto, Item

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['loja', 'categoria', 'estado', 'preco', 'descricao']

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'preco', 'condicao', 'tamanho', 'foto', 'tipo_produto']

class CheckoutForm(forms.Form):
    nome_completo = forms.CharField(max_length=100)
    endereco = forms.CharField(max_length=255)
    cidade = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    cep = forms.CharField(max_length=10)
    forma_pagamento = forms.ChoiceField(choices=[
        ('boleto', 'Boleto'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
    ])
    numero_cartao = forms.CharField(max_length=16, required=False)
    validade_cartao = forms.CharField(max_length=5, required=False)
    cvv_cartao = forms.CharField(max_length=3, required=False)

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'preco']

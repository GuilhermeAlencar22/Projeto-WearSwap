from django import forms

class ProdutoForm(forms.Form):
    loja = forms.CharField(label='Nome da loja', max_length=100)
    categoria = forms.CharField(label='Categoria do produto', max_length=100)
    estado = forms.CharField(label='Estado do produto', max_length=100)
    preco = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2)
    descricao = forms.CharField(label='Descrição do produto', max_length=100)




class SearchForm(forms.Form):
    keyword = forms.CharField(label='Palavra-chave', max_length=100)
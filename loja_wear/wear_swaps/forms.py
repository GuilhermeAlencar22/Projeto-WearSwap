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

class CheckoutForm(forms.Form):
    nome_completo = forms.CharField(max_length=100, label='Nome Completo')
    endereco = forms.CharField(max_length=255, label='Endereço')
    cidade = forms.CharField(max_length=100, label='Cidade')
    estado = forms.CharField(max_length=100, label='Estado')
    cep = forms.CharField(max_length=10, label='CEP')
    opcoes_pagamento = [
        ('credito', 'Cartão de Crédito'),
        ('debito', 'Cartão de Débito'),
    ]
    forma_pagamento = forms.ChoiceField(choices=opcoes_pagamento, label='Forma de Pagamento')
    numero_cartao = forms.CharField(max_length=16, label='Número do Cartão', required=False)
    validade_cartao = forms.CharField(max_length=5, label='Validade do Cartão (MM/AA)', required=False)
    cvv_cartao = forms.CharField(max_length=3, label='CVV', required=False)

    def clean(self):
        cleaned_data = super().clean()
        forma_pagamento = cleaned_data.get('forma_pagamento')
        numero_cartao = cleaned_data.get('numero_cartao')
        validade_cartao = cleaned_data.get('validade_cartao')
        cvv_cartao = cleaned_data.get('cvv_cartao')

        if forma_pagamento in ['credito', 'debito']:
            if not numero_cartao:
                self.add_error('numero_cartao', 'Este campo é obrigatório.')
            if not validade_cartao:
                self.add_error('validade_cartao', 'Este campo é obrigatório.')
            if not cvv_cartao:
                self.add_error('cvv_cartao', 'Este campo é obrigatório.')
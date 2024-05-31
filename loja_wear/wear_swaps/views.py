from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import RegisteredUser, Produto, ClothingItem, Compra, Item, ItemCarrinho, Carrinho
from .forms import ProdutoForm, SearchForm, ItemForm, CheckoutForm  # Importando CheckoutForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.html import escape

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = RegisteredUser.objects.get(username=username)
        except RegisteredUser.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('homepage')
        else:
            error_message = "Nome de usuário ou senha incorretos."
            return render(request, 'wear_swap/login.html', {'error_message': error_message})
    else:
        return render(request, 'wear_swap/login.html')

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Processar o formulário e salvar os dados
            nome_completo = form.cleaned_data['nome_completo']
            endereco = form.cleaned_data['endereco']
            cidade = form.cleaned_data['cidade']
            estado = form.cleaned_data['estado']
            cep = form.cleaned_data['cep']
            forma_pagamento = form.cleaned_data['forma_pagamento']
            numero_cartao = form.cleaned_data['numero_cartao']
            validade_cartao = form.cleaned_data['validade_cartao']
            cvv_cartao = form.cleaned_data['cvv_cartao']

            # Salvar a compra no banco de dados (você precisa criar a lógica para isso)

            messages.success(request, 'Compra realizada com sucesso!')
            return redirect('compra_sucesso')
    else:
        form = CheckoutForm()
    return render(request, 'wear_swap/checkout.html', {'form': form})

def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return redirect('carrinho')

def homepage(request):
    form = SearchForm(request.GET or None)
    resultados = None
    produto_id = None

    try:
        ultimo_produto = Produto.objects.latest('id')
        produto_id = ultimo_produto.id
    except Produto.DoesNotExist:
        produto_id = None

    if request.method == 'GET' and form.is_valid():
        keyword = form.cleaned_data['keyword']
        resultados = Item.objects.filter(descricao__icontains=keyword)

    categoria = request.GET.get('categoria')
    if categoria:
        itens = Item.objects.filter(tipo_produto=categoria)
    else:
        itens = Item.objects.all()

    categorias = Item.TIPOS_PRODUTO

    context = {
        'form': form,
        'resultados': resultados,
        'produto_id': produto_id,
        'itens': itens,
        'categorias': categorias
    }

    return render(request, 'wear_swap/homepage.html', context)

def filtro(request):
    return render(request, 'wear_swap/filtro.html')

def adicionar_ao_carrinho(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    item_carrinho, created = ItemCarrinho.objects.get_or_create(usuario=request.user, item=item)

    if not created:
        item_carrinho.quantidade += 1
        item_carrinho.save()

    messages.success(request, 'Item adicionado ao carrinho com sucesso!')
    return redirect('homepage')

@login_required
def ver_carrinho(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    itens_carrinho = ItemCarrinho.objects.filter(usuario=request.user)
    return render(request, 'wear_swap/carrinho.html', {'itens_carrinho': itens_carrinho})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        if RegisteredUser.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso. Por favor, escolha outro.')
            return render(request, 'wear_swap/register.html')

        new_user = RegisteredUser.objects.create_user(username=username, password=password)
        login(request, new_user)
        messages.success(request, 'Registro realizado com sucesso! Bem-vindo ao nosso site.')
        return redirect('login')

    return render(request, 'wear_swap/register.html')

def ajuda_view(request):
    return render(request, 'wear_swap/ajuda_ao_cliente.html')

def ver_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            novo_produto = Produto(
                loja=form.cleaned_data['loja'],
                categoria=form.cleaned_data['categoria'],
                estado=form.cleaned_data['estado'],
                preco=form.cleaned_data['preco'],
                descricao=form.cleaned_data['descricao']
            )
            novo_produto.save()
            return redirect('produto_inserido', produto_id=novo_produto.id)
        else:
            return render(request, 'wear_swap/ver_produto.html', {'form': form})
    else:
        form = ProdutoForm()
        return render(request, 'wear_swap/ver_produto.html', {'form': form})

def produto_inserido(request, produto_id):
    return render(request, 'wear_swap/produto_inserido.html', {'produto_id': produto_id})

def ver_loja_criada(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'wear_swap/loja_criada.html', {'produto': produto})

def ver_item(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            novo_item = form.save(commit=False)
            novo_item.produto = produto
            novo_item.save()
            return redirect('item_inserido', produto_id=produto.id)
    else:
        form = ItemForm()
    return render(request, 'wear_swap/ver_item.html', {'form': form, 'produto': produto})

def item_inserido(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            novo_item = form.save(commit=False)
            novo_item.produto = produto
            novo_item.save()
            return redirect('produto_inserido', produto_id=produto.id)
    else:
        form = ItemForm()
    return render(request, 'wear_swap/item_inserido.html', {'form': form, 'produto': produto})

def itens_adicionados(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    itens = produto.item_set.all()
    return render(request, 'wear_swap/itens_adicionados.html', {'produto': produto, 'itens': itens})

def clothing_list(request):
    clothing_items = ClothingItem.objects.all()
    return render(request, 'clothing/clothing_list.html', {'clothing_items': clothing_items})

def configuracoes_view(request):
    return render(request, 'wear_swap/configuracoes.html')

@login_required
def alterar_senha_view(request):
    if request.method == 'POST':
        senha_antiga = request.POST.get('senha_antiga')
        nova_senha = request.POST.get('nova_senha')
        confirmar_nova_senha = request.POST.get('confirmar_nova_senha')

        if check_password(senha_antiga, request.user.password):
            if nova_senha == confirmar_nova_senha:
                request.user.set_password(nova_senha)
                request.user.save()
                messages.success(request, "Senha alterada com sucesso.")
                return redirect('homepage')
            else:
                messages.error(request, "A nova senha e a confirmação não coincidem.")
        else:
            messages.error(request, "Senha antiga incorreta.")

    return render(request, 'wear_swap/alterar_senha.html')

def historico_compras(request):
    if request.user.is_authenticated:
        compras = Compra.objects.filter(usuario=request.user).order_by('-data_compra')
        return render(request, 'wear_swap/historico_compras.html', {'compras': compras})
    else:
        return redirect('login')

def dados_pessoais_view(request):
    user_profile = RegisteredUser.objects.get(username=request.user.username)
    if request.user.is_authenticated:
        return render(request, 'wear_swap/dados_pessoais.html', {'user_profile': user_profile})
    else:
        pass

@require_POST
def delete_account(request):
    user = request.user
    username = user.username
    user.delete()
    logout(request)
    messages.success(request, f'Sua conta, {username}, foi excluída com sucesso.')
    return redirect('account_deleted')

def account_deleted(request):
    message = messages.get_messages(request)
    return render(request, 'account_deleted.html', {'messages': message})

def compra_sucesso_view(request):
    return render(request, 'wear_swap/compra_sucesso.html')

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import RegisteredUser, Produto, ClothingItem
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import ProdutoForm, SearchForm # type: ignore
from django.urls import path
from .models import Compra
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.html import escape


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Username recebido:", username)
        print("Password recebido:", password)

        # Verifica se o usuário existe no banco de dados
        try:
            user = RegisteredUser.objects.get(username=username)
            print("Usuário encontrado no banco de dados:", user)
        except RegisteredUser.DoesNotExist:
            user = None

        # Autentica o usuário
        if user is not None and user.check_password(password):
            print("Usuário autenticado com sucesso:", user.username)
            login(request, user)
            return redirect('homepage')  # Redireciona para a página inicial após o login
        else:
            error_message = "Nome de usuário ou senha incorretos."
            print("Falha na autenticação")
            return render(request, 'wear_swap/login.html', {'error_message': error_message})
    else:
        return render(request, 'wear_swap/login.html')



def homepage(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            # Filtra os produtos com base na palavra-chave
            resultados = Produto.objects.filter(descricao__icontains=keyword)
            return render(request, 'wear_swap/homepage.html', {'form': form, 'resultados': resultados})
    else:
        form = SearchForm()
    return render(request, 'wear_swap/homepage.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']  # Alterado para 'password1'
        # Crie um novo objeto do modelo de usuário com os dados fornecidos
        new_user = RegisteredUser.objects.create_user(username=username, password=password)
        # Faça login automaticamente no novo usuário
        login(request, new_user)
        return redirect('login')  # Redireciona para a página de login após o registro
    else:
        return render(request, 'wear_swap/register.html')  # Renderize a página de registro
    


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
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'wear_swap/loja_criada.html', {'produto': produto})



def filtro(request):
    return render(request,'wear_swap/filtro.html')
def clothing_list(request):
    clothing_items = ClothingItem.objects.all()
    return render(request, 'clothing/clothing_list.html', {'clothing_items': clothing_items})



def configuracoes_view(request):
    return render(request, 'wear_swap/configuracoes.html')


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

@login_required
def alterar_senha_view(request):
    if request.method == 'POST':
        senha_antiga = request.POST.get('senha_antiga')
        nova_senha = request.POST.get('nova_senha')
        confirmar_nova_senha = request.POST.get('confirmar_nova_senha')

        # Verificar se a senha antiga está correta para o usuário atual
        if check_password(senha_antiga, request.user.password):
            # Verificar se a nova senha e a confirmação são iguais
            if nova_senha == confirmar_nova_senha:
                # Definir a nova senha para o usuário atual
                request.user.set_password(nova_senha)
                request.user.save()
                # Redirecionar para uma página de sucesso ou para a página inicial
                messages.success(request, "Senha alterada com sucesso.")
                return redirect('homepage')
            else:
                # Nova senha e confirmação não são iguais, exibir mensagem de erro
                messages.error(request, "A nova senha e a confirmação não coincidem.")
        else:
            # Senha antiga incorreta, exibir mensagem de erro
            messages.error(request, "Senha antiga incorreta.")

    # Renderize o template alterar_senha.html
    return render(request, 'wear_swap/alterar_senha.html')



def historico_compras(request):
    if request.user.is_authenticated:
        compras = Compra.objects.filter(usuario=request.user).order_by('-data_compra')
        return render(request, 'wear_swap/historico_compras.html', {'compras': compras})
    else:
        return redirect('login')

def dados_pessoais_view(request):
    user_profile = RegisteredUser.objects.get(username=user_profile)
    if request.user.is_authenticated:
        user_profile = RegisteredUser.objects.get(username=request.user.username)
        return render(request, 'wear_swap/dados_pessoais.html', {'user_profile': user_profile})
    else:
        # Trate o caso em que o usuário não está autenticado
        # Você pode redirecionar para a página de login ou exibir uma mensagem de erro
        pass


@require_POST
def delete_account(request):
    user = request.user
    username = user.username  # Captura o nome de usuário para mostrar na mensagem
    user.delete()
    logout(request)
    messages.success(request, f'Sua conta, {username}, foi excluída com sucesso.')
    return redirect('account_deleted')  # Redireciona para a página de confirmação

def account_deleted(request):
    message = messages.get_messages(request)  # Recupera mensagens para passar para o template
    return render(request, 'account_deleted.html', {'messages': message})
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import RegisteredUser, Produto, ClothingItem
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import ProdutoForm, SearchForm
from django.urls import path
from .models import Compra
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required





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
            return render(request, 'wear_swaps/login.html', {'error_message': error_message})
    else:
        return render(request, 'wear_swaps/login.html')



def homepage(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            # Filtra os produtos com base na palavra-chave
            resultados = Produto.objects.filter(descricao__icontains=keyword)
            return render(request, 'wear_swaps/homepage.html', {'form': form, 'resultados': resultados})
    else:
        form = SearchForm()
    return render(request, 'wear_swaps/homepage.html', {'form': form})

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
        return render(request, 'wear_swaps/register.html')  # Renderize a página de registro
    


def ver_produto(request):
   if request.method == "GET":
       form = ProdutoForm()
       return render(request, 'wear_swaps/ver_produto.html', {'form': form})
   elif request.method == "POST":
       form = ProdutoForm(request.POST)
       if form.is_valid():
           # Cria uma instância do modelo Produto mas não salva ainda no banco de dados
           novo_produto = Produto(
               loja=form.cleaned_data['loja'],
               categoria=form.cleaned_data['categoria'],
               estado=form.cleaned_data['estado'],
               preco=form.cleaned_data['preco'],
               descricao=form.cleaned_data['descricao']
           )
          
           # Salva o novo produto no banco de dados
           novo_produto.save()
           # Redireciona para a página de confirmação
           return redirect('produto_inserido')
       else:
           # Se o formulário for inválido, renderize a página novamente com o formulário
           return render(request, 'wear_swaps/produto_inserido.html', {'form': form})
      


def produto_inserido(request):
   return render(request, 'wear_swaps/produto_inserido.html')



def filtro(request):
    return render(request,'wear_swaps/filtro.html')
def clothing_list(request):
    clothing_items = ClothingItem.objects.all()
    return render(request, 'clothing/clothing_list.html', {'clothing_items': clothing_items})



def configuracoes_view(request):
    return render(request, 'wear_swaps/configuracoes.html')


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
    return render(request, 'wear_swaps/alterar_senha.html')



def historico_compras(request):
    if request.user.is_authenticated:
        compras = Compra.objects.filter(usuario=request.user).order_by('-data_compra')
        return render(request, 'wear_swaps/historico_compras.html', {'compras': compras})
    else:
        return redirect('login')

def dados_pessoais_view(request):
    user_profile = RegisteredUser.objects.get(username=user_profile)
    if request.user.is_authenticated:
        user_profile = RegisteredUser.objects.get(username=request.user.username)
        return render(request, 'wear_swaps/dados_pessoais.html', {'user_profile': user_profile})
    else:
        # Trate o caso em que o usuário não está autenticado
        # Você pode redirecionar para a página de login ou exibir uma mensagem de erro
        pass
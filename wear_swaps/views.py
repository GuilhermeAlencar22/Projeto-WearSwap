from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import RegisteredUser, Produto, ClothingItem
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import ProdutoForm, SearchForm
from django.urls import path



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
            novo_produto = Produto(
                loja=form.cleaned_data['loja'],
                categoria=form.cleaned_data['categoria'],
                estado=form.cleaned_data['estado'],
                preco=form.cleaned_data['preco'],
                descricao=form.cleaned_data['descricao']
            )
            novo_produto.save()
            # Passa o ID do produto criado para a próxima página
            return redirect('produto_inserido', produto_id=novo_produto.id)
        else:
            return render(request, 'wear_swaps/ver_produto.html', {'form': form})


def ver_loja_criada(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'wear_swaps/loja_criada.html', {'produto': produto})

def produto_inserido(request, produto_id):
    # Adiciona um botão para visualizar a loja criada
    return render(request, 'wear_swaps/produto_inserido.html', {'produto_id': produto_id})




def filtro(request):
    return render(request,'wear_swaps/filtro.html')
def clothing_list(request):
    clothing_items = ClothingItem.objects.all()
    return render(request, 'clothing/clothing_list.html', {'clothing_items': clothing_items})

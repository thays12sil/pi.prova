from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserBlogCreationForm, UserBlogEditForm
from .models import UserBlog
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Loga o usuário
            return redirect('gerencia:gerencia_inicial')  # Redireciona após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request) 
    return redirect('usuarios:login')  



def register(request):
    if request.method == 'POST':
        form = UserBlogCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('usuarios:login')  
    else:
        form = UserBlogCreationForm()

    return render(request, 'usuarios/register.html', {'form': form})


def lista_usuarios(request):
    usuarios_lista = UserBlog.objects.all().order_by('username')
    paginator = Paginator(usuarios_lista, 5)  # 10 usuários por página
    
    page = request.GET.get('page', 1)
    
    usuarios = paginator.page(page)
   
    
    return render(request, 'usuarios/lista_usuario.html', {
        'usuarios': usuarios
    })


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserBlogCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UserBlogCreationForm()
    
    return render(request, 'usuarios/form.html', {
        'form': form,
        'titulo': 'Cadastrar Usuário',
        'botao': 'Cadastrar'
    })


@login_required
def editar_usuario(request, id):
    usuario = get_object_or_404(UserBlog, id=id)
    
    if request.method == 'POST':
        form = UserBlogEditForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UserBlogEditForm(instance=usuario)
    
    return render(request, 'usuarios/form.html', {
        'form': form,
        'usuario': usuario
    })
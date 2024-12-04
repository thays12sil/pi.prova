from django.shortcuts import render
from .models import Modalidade, Curso, Aluno

# Create your views here.
def index(request):
    cursos = Curso.objects.all() # Select do django
    contexto = {
        'lista': cursos,
    }
    return render(request, 'curso/index.html',contexto)


def detalhe_curso(request, curso_id):
    curso_selecionado = Curso.objects.get(id=curso_id)
    alunos = Aluno.objects.filter(curso=curso_selecionado)
    contexto = {
        'curso': curso_selecionado,
        'alunos': alunos
    }
    return render(request, 'curso/detalhe_curso.html',contexto)

def pagina_sobre(request):
    return render(request, 'curso/sobre.html')

def pagina_teste(request):
    return render(request, 'curso/teste.html')

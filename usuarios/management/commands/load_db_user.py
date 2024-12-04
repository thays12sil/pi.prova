import random
import string
from django.core.management.base import BaseCommand
from usuarios.models import UserBlog

# Função para gerar um CPF aleatório de 11 dígitos
def generate_random_cpf():
    return ''.join(random.choices(string.digits, k=11))

# Lista de nomes e usernames para os usuários
USER_DATA = [
    {"nome": "Jeferson Queiroga", "username": "queiroga"},
    {"nome": "Maria Silva", "username": "maria.silva"},
    {"nome": "João Souza", "username": "joao.souza"},
    {"nome": "Ana Costa", "username": "ana.costa"},
    {"nome": "Carlos Pereira", "username": "carlos.pereira"},
    {"nome": "Paula Fernandes", "username": "paula.fernandes"},
]

class Command(BaseCommand):
    help = 'Carrega usuários no banco de dados com dados pré-definidos e CPF aleatório'

    def handle(self, *args, **options):
        for user_data in USER_DATA:
            username = user_data["username"]
            nome = user_data["nome"]
            
            # Verifica se o usuário já existe para evitar duplicações
            if not UserBlog.objects.filter(username=username).exists():
                # Cria o usuário com os campos nome, username, cpf e e-mail
                UserBlog.objects.create_user(
                    username=username,
                    password="ifrn12345",
                    cpf=generate_random_cpf(),
                    email=f"{username}@exemplo.com",
                    first_name=nome.split()[0],
                    last_name=nome.split()[-1]
                )
                self.stdout.write(self.style.SUCCESS(f"Usuário '{nome}' ({username}) criado com sucesso!"))
            else:
                self.stdout.write(self.style.WARNING(f"Usuário '{username}' já existe."))
        
        self.stdout.write(self.style.SUCCESS("Processo de criação de usuários concluído!"))

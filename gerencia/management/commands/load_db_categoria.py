from django.core.management.base import BaseCommand
from gerencia.models import Categoria  # Importe o modelo Categoria, ajustando o caminho conforme necessário

# Lista de nomes de categorias para serem carregadas no banco de dados
CATEGORY_NAMES = [
    "Política",
    "Economia",
    "Esportes",
    "Tecnologia",
    "Entretenimento",
    "Educação",
    "Saúde",
    "Cultura",
]

class Command(BaseCommand):
    help = 'Carrega categorias no banco de dados'

    def handle(self, *args, **options):
        for category_name in CATEGORY_NAMES:
            # Verifica se a categoria já existe para evitar duplicação
            if not Categoria.objects.filter(nome=category_name).exists():
                Categoria.objects.create(nome=category_name)
                self.stdout.write(self.style.SUCCESS(f"Categoria '{category_name}' criada com sucesso!"))
            else:
                self.stdout.write(self.style.WARNING(f"Categoria '{category_name}' já existe."))
        
        self.stdout.write(self.style.SUCCESS("Processo de criação de categorias concluído!"))

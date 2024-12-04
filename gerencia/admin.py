from django.contrib import admin
from .models import Noticia,Categoria

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao',)
    search_fields = ('titulo', )
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

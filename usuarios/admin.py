from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserBlog

class UserBlogAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')}),
    )

admin.site.register(UserBlog, UserBlogAdmin)

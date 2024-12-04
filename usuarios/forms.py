from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserBlog

class UserBlogCreationForm(UserCreationForm):
    cpf = forms.CharField(max_length=11, required=True, help_text="Digite seu CPF sem pontos ou traços.")
    nome_cidade = forms.CharField(max_length=100, required=False)
    nome_mae = forms.CharField(max_length=100, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    nome_bairro = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classe form-control para os campos padrão do UserCreationForm
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome_cidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome_bairro'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome_mae'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = UserBlog
        fields = ('username', 'cpf', 'email', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro','password1', 'password2')


class UserBlogEditForm(forms.ModelForm):
    cpf = forms.CharField(
        max_length=11,
        required=True,
        help_text="Digite seu CPF sem pontos ou traços.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_cidade = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_mae = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    endereco = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_bairro = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classe form-control para campos padrão
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = UserBlog
        fields = ('username', 'email', 'cpf', 'nome_cidade', 'nome_mae', 
                 'endereco', 'nome_bairro')
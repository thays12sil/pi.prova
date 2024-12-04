

# Projeto Django - Guia de Instalação no Windows

## **Passo 1: Clonar o projeto**

Abra o **Prompt de Comando** ou **PowerShell** e execute:
```bash
git https://github.com/JefersonQueiroga/Blog2024.git
cd Blog2024
```

---

## **Passo 2: Criar e ativar o ambiente virtual**

No diretório do projeto, crie um ambiente virtual chamado `venv`:
```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Prompt de Comando:**
  ```bash
  venv\Scripts\activate
  ```

- **PowerShell:**
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

**Nota:** Se você receber um erro ao ativar o ambiente no PowerShell, use o comando abaixo para permitir a execução de scripts:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## **Passo 3: Instalar as dependências**

Com o ambiente virtual ativado, instale todas as dependências listadas em `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## **Passo 4: Configurar o banco de dados**

Rode os seguintes comandos para criar e aplicar as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **Passo 5: Criar um superusuário**

Para acessar o admin do Django, crie um superusuário:
```bash
python manage.py createsuperuser
```

---

## **Passo 6: Executar o servidor de desenvolvimento**

Inicie o servidor local:
```bash
python manage.py runserver
```

Abra o navegador e acesse [http://127.0.0.1:8000](http://127.0.0.1:8000).

---



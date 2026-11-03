comandos:
 
# CRIAR UMA VENV  :

- python3 -m venv .venv 

# INICICAR A VENV

- source .venv/bin/activate

# CRIAR A BASE "SIMPLES" DO DJANGO

- django-admin startproject projeto 

# COMANDO PARA INSTALAR O DJANGO

- pip install django

# COMANDO PARA PODER RODAR O DJANGO WEB

- python3 manage.py runserver 8001 (ou a porta que vc definir na hr)


# PASTAS E ARQUIVOS DO PROJETO DJANGO

Estrutura criada com `django-admin startproject projeto .`:

```text
curso_Django_pago-projeto1/
├── .venv/                 # Ambiente virtual: guarda o Python e as bibliotecas do projeto
├── projeto/               # Pacote principal de configuração do Django
│   ├── __init__.py        # Marca projeto como pacote Python
│   ├── asgi.py            # Ponto de entrada para servidores ASGI e aplicações assíncronas
│   ├── settings.py        # Configurações: apps, banco de dados, idioma, segurança e arquivos estáticos
│   ├── urls.py            # Rotas: associa endereços web às views; inicialmente contém /admin/
│   └── wsgi.py            # Ponto de entrada para servidores WSGI tradicionais
├── .gitignore             # Lista arquivos e pastas que o Git deve ignorar
├── db.sqlite3             # Banco SQLite local, criado após as migrações
└── manage.py              # Utilitário para executar comandos Django, como runserver e migrate
```

O ponto final (`.`) no comando `django-admin startproject projeto .` faz o
Django criar `manage.py` e a pasta `projeto/` dentro da pasta atual.

Outros itens que podem aparecer:

- `__pycache__/` # Cache de bytecode criado pelo Python; pode ser recriado automaticamente.
- `migrations/` # Pasta criada dentro de um app Django para guardar alterações do modelo do banco.
- `templates/` # Pasta que pode ser criada para guardar templates HTML.
- `static/` # Pasta que pode ser criada para CSS, JavaScript e imagens.

# COMO USAR O DEBUG NO VS CODE

1. Abra no VS Code a pasta raiz do repositório, que contém `.vscode/`.
2. Instale/ative as extensões **Python** e **Python Debugger** da Microsoft.
3. Abra o arquivo Python onde quer investigar o código e clique ao lado do número
   de uma linha executável para criar um breakpoint (ponto vermelho).
4. Abra **Executar e Depurar** na barra lateral, selecione **Python: Django**
   e pressione `F5`. A configuração em `.vscode/launch.json` inicia
   `curso_Django_pago-projeto1/manage.py runserver 8002`.
5. Acesse `http://127.0.0.1:8002/` no navegador. Quando a execução atingir um
   breakpoint, ela pausa no VS Code; use **Continuar**, **Passo a passo** e
   **Parar** na barra de depuração para controlar a execução.

Se a porta 8002 já estiver em uso, pare o outro servidor ou altere a porta
`8002` nos argumentos de `.vscode/launch.json`. Para encerrar a sessão de debug,
clique em **Parar** ou pressione `Shift+F5`.
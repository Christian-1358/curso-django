# Documentação Django

## Navegação rápida

🟢 **Preparar e executar o projeto**

- [Criar o ambiente virtual](#criar-uma-venv)
- [Ativar o ambiente virtual](#iniciar-a-venv)
- [Criar o projeto Django](#criar-a-base-simples-do-django)
- [Instalar o Django](#comando-para-instalar-o-django)
- [Iniciar o servidor](#comando-para-poder-rodar-o-django-web)

🔵 **Criar e entender um app**

- [Criar o app `recipes` com `startapp`](#criar-um-app-django)
- [Entender os arquivos Python do app](#arquivos-python-do-app-recipes)

🟣 **Conhecer a estrutura do projeto**

- [Pastas e arquivos do projeto](#pastas-e-arquivos-do-projeto-django)

🟠 **Rotas e respostas**

- [Rotas com `path()` e views](#rotas-com-path-e-views)
- [Separar rotas com `include()`](#separar-rotas-com-include)
- [Usar `render()` para enviar dados ao HTML](#usar-render-para-enviar-dados-ao-html)
- [Reutilizar templates com `{% include %}`](#reutilizar-templates-com-include)
- [Entender `request`](#request)
- [Entender `HttpResponse`](#httpresponse)
- [Consultar códigos de status HTTP](#link-para-poder-ver-os-codigos-de-erro-em-web)

🔴 **Ferramentas de desenvolvimento**

- [Usar o debug no VS Code](#como-usar-o-debug-no-vs-code)
- [Configurar sugestões do Python e Pylance](#pylance-e-python-no-vs-code)

---

# CRIAR UMA VENV

- python3 -m venv .venv 

# INICIAR A VENV

- source .venv/bin/activate

# CRIAR A BASE "SIMPLES" DO DJANGO

- django-admin startproject projeto 

# COMANDO PARA INSTALAR O DJANGO

- pip install django

# COMANDO PARA PODER RODAR O DJANGO WEB

- python3 manage.py runserver 8001 (ou a porta que vc definir na hr)

# CRIAR UM APP DJANGO

Um app é uma parte do projeto responsável por um conjunto de funcionalidades.
Por exemplo, o app `recipes` pode cuidar das receitas do site. Criar um app
separa o código por assunto e facilita a organização do projeto.

Execute o comando na pasta onde está o arquivo `manage.py`:

```bash
python3 manage.py startapp recipes
```

O comando é dividido assim:

- `python3` executa o programa Python.
- `manage.py` dá acesso aos comandos do projeto Django atual.
- `startapp` pede ao Django para criar a estrutura inicial de um app.
- `recipes` é o nome do app; esse nome também será o da pasta criada.

O Django cria a pasta `recipes/` com arquivos iniciais, como `models.py`,
`views.py`, `admin.py` e `apps.py`, além da pasta `migrations/`. O comando cria
os arquivos, mas ainda é preciso avisar ao projeto que ele deve carregar esse
app.

Para registrar o app, abra `projeto/settings.py` e adicione
`'recipes.apps.RecipesConfig',` à lista `INSTALLED_APPS`. Faça isso uma única
vez para cada app. O comando `startapp` também deve ser executado apenas uma
vez para esse nome; se a pasta `recipes/` já existir, não o execute novamente.

**Observação:** também é possível criar a pasta e os arquivos do app
manualmente. Porém, criar apenas a pasta não basta: é preciso montar a
estrutura necessária do Django (incluindo arquivos como `apps.py` e
`migrations/__init__.py`) e registrar o app em `INSTALLED_APPS`. Usar
`startapp` é o caminho recomendado para gerar essa estrutura inicial
automaticamente.

# ARQUIVOS PYTHON DO APP `recipes`

O comando `python3 manage.py startapp recipes` cria arquivos para separar as
responsabilidades do app:

- `recipes/__init__.py`: indica ao Python que `recipes` é um pacote que pode
  ser importado. Normalmente fica vazio.
- `recipes/admin.py`: permite registrar modelos para gerenciá-los pela área
  administrativa do Django.
- `recipes/apps.py`: contém a configuração do app. `RecipesConfig` identifica
  o nome do app e outras opções; essa classe pode ser usada em `INSTALLED_APPS`.
- `recipes/models.py`: define os modelos, que representam os dados do app e
  geralmente correspondem a tabelas no banco de dados.
- `recipes/tests.py`: contém testes automatizados para verificar se o app
  funciona como esperado.
- `recipes/views.py`: contém as views, que recebem requisições e retornam
  respostas, como páginas HTML.
- `recipes/migrations/__init__.py`: permite que a pasta de migrações seja
  reconhecida como um pacote Python.
- `recipes/migrations/`: guarda arquivos Python de migração. Eles registram
  alterações nos modelos do banco de dados. O Django cria esses arquivos com
  `python3 manage.py makemigrations` e aplica as alterações com
  `python3 manage.py migrate`.


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

# ROTAS COM `path()` E VIEWS

As rotas dizem ao Django qual código executar quando alguém acessa um endereço
do site. Elas ficam normalmente no arquivo `urls.py`.

Por exemplo:

```python
from django.contrib import admin
from django.urls import path
from minha_app.views import myView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', myView),
]
```

Entendendo cada parte:

- `path()` cria uma rota. O primeiro valor é o caminho que será acessado no
  navegador; o segundo indica o código que o Django deve chamar.
- `path('admin/', admin.site.urls)` abre a área de administração do Django no
  endereço `http://127.0.0.1:8000/admin/`.
- `path('inicio/', myView)` chama a função `myView` quando alguém acessa
  `http://127.0.0.1:8000/inicio/`.
- Em geral, escrevemos o caminho sem a barra inicial e com a barra final,
  como `'inicio/'`.
- `urlpatterns` é a lista de rotas que o Django consulta.

## SEPARAR ROTAS COM `include()`

Em projetos com vários apps, é útil deixar cada app responsável por suas
próprias rotas. O arquivo `projeto/urls.py` fica com as rotas principais e usa
`include()` para encaminhar as demais para o arquivo de URLs do app.

No arquivo `projeto/urls.py`, importe `include` e conecte as rotas de
`recipes`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
```

No app, crie o arquivo `recipes/urls.py` e defina nele as rotas do app:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
    path('contato/', views.contato),
]
```

`include('recipes.urls')` diz ao Django para continuar procurando a rota em
`recipes/urls.py`. Como o prefixo usado no projeto é `''` (vazio), os caminhos
do app ficam disponíveis como `/`, `/sobre/` e `/contato/`. Se, por exemplo,
o prefixo fosse `'receitas/'`, eles ficariam `/receitas/`,
`/receitas/sobre/` e `/receitas/contato/`.

Assim, `projeto/urls.py` centraliza a ligação entre o projeto e os apps, e cada
app pode manter suas rotas em seu próprio `urls.py`.

## USAR `render()` PARA ENVIAR DADOS AO HTML

`render()` é uma função auxiliar do Django, importada de
`django.shortcuts`. Ela combina uma requisição, um template e os dados que a
view quer apresentar. O Django processa o template e devolve uma resposta HTTP
com o HTML pronto para o navegador.

Em termos simples:

```text
render(request, caminho_do_template, contexto)
```

- `request`: a requisição atual, recebida pela view.
- `caminho_do_template`: o caminho do arquivo HTML relativo à pasta
  `templates/`.
- `contexto`: um dicionário opcional com os dados que o template poderá usar.

### 1. Importe `render` e envie dados pela view

No seu exemplo atual, a view envia o valor `'Christian'` com a chave `'name'`:

No arquivo `recipes/views.py`:

```python
from django.shortcuts import render


def home(request):
    return render(
        request,
        'recipes/home.html',
        context={
            'name': 'Christian',
        },
    )
```

O `from django.shortcuts import render` importa a função. O argumento
`context=` recebe um dicionário: a chave `'name'` será o nome da variável no
template, e o valor `'Christian'` será o conteúdo dessa variável. O segundo
argumento aponta para `recipes/templates/recipes/home.html`.

Também é possível criar o dicionário antes e passá-lo como terceiro argumento
posicional:

```python
contexto = {'name': 'Christian'}
return render(request, 'recipes/home.html', contexto)
```

As duas formas fazem a mesma coisa. Usar `context=` deixa explícito que o
dicionário contém os dados que serão disponibilizados ao HTML.

### 2. Crie o template HTML

O caminho do template no `render()` corresponde ao arquivo
`recipes/templates/recipes/home.html`. Com `APP_DIRS = True` nas configurações
padrão do Django, o Django procura templates dentro da pasta `templates/` do
app. Para exibir o dado enviado pela view:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recipes</title>
</head>
<body>
  <h1>recipes {{ name }}</h1>
</body>
</html>
```

`{{ name }}` é uma variável do template. O Django procura a chave `name` no
dicionário `context` e substitui a expressão pelo valor correspondente. Com o
exemplo acima, o navegador exibe **recipes Christian**. Se a chave não for
enviada pela view, a variável normalmente aparece vazia.

Para acrescentar outros valores, adicione mais pares de chave e valor ao
dicionário e use as chaves no HTML:

```python
context={
    'name': 'Christian',
    'titulo': 'Minhas receitas',
}
```

```html
<title>{{ titulo }}</title>
<h1>{{ titulo }} de {{ name }}</h1>
```

Assim, a view fornece os dados, e o template HTML decide onde e como
apresentá-los.

O Django escapa automaticamente valores exibidos por `{{ ... }}`; evite
desativar essa proteção para dados fornecidos por usuários. Se depois você
buscar dados no banco, também pode incluí-los no contexto. Por exemplo:

```python
from .models import Receita

receitas = Receita.objects.all()
return render(
    request,
    'recipes/home.html',
    context={'name': 'Christian', 'receitas': receitas},
)
```

Nesse caso, o template pode percorrer `receitas` com `{% for %}`, assim como no
exemplo:

```django
<ul>
  {% for receita in receitas %}
    <li>{{ receita }}</li>
  {% empty %}
    <li>Nenhuma receita encontrada.</li>
  {% endfor %}
</ul>
```

## REUTILIZAR TEMPLATES COM `{% include %}`

O template tag `{% include %}` insere o conteúdo processado de outro template
no ponto em que aparece. Ele é útil para reaproveitar partes da página, como
cabeçalho, navegação ou rodapé.

Por exemplo, para incluir o arquivo
`recipes/templates/recipes/partials/head.html` em
`recipes/templates/recipes/pages/home.html`, use o caminho relativo à pasta
`templates/` do app:

```django
{% include 'recipes/partials/head.html' %}
```

O nome do template precisa estar entre aspas; `{% include "" %}` não informa
qual arquivo deve ser incluído. O template incluído recebe o contexto atual por
padrão, então pode acessar variáveis como `{{ name }}` que foram enviadas pela
view.

Este uso é diferente de `include()` em `projeto/urls.py`: a função Python
`include()` encaminha rotas para outro arquivo `urls.py`, enquanto
`{% include %}` reutiliza um template HTML.

### 3. Conecte a view à URL

Em `recipes/urls.py`, associe a página inicial à view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Se `projeto/urls.py` incluir `recipes.urls` com
`path('', include('recipes.urls'))`, a página será exibida ao acessar `/`.

**Resumo do fluxo:** o navegador solicita uma URL → Django encontra a rota →
a view prepara o contexto → `render()` processa o template com esses dados e
cria a resposta HTTP → o navegador recebe e apresenta o HTML.

Uma **view** é o código que responde à visita a uma rota. Ela pode buscar
informações, fazer algum processamento e devolver uma resposta. Por exemplo,
no arquivo `views.py` de `minha_app`:

```python
from django.http import HttpResponse


def myView(request):
    return HttpResponse("Olá! Esta é a página inicial.")
```

O parâmetro `request` contém informações sobre a solicitação que chegou ao
Django. `HttpResponse` devolve um texto ao navegador. Para usar essa view, o
`urls.py` importa `myView` e liga a função ao caminho `'inicio/'` com `path()`.

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



# REQUEST 

- O que o cliente faz


# HttpResponse

- O que o servidor responde

# LINK PARA PODER VER OS CODIGOS DE ERRO EM WEB

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status

# PYLANCE E PYTHON NO VS CODE

As extensões Python e Pylance oferecem recursos como o preenchimento automático
de código. Para praticar sem essas sugestões, desative-as no arquivo
`settings.json`:

```json
{
  "[python]": {
    "editor.quickSuggestions": {
      "other": "off",
      "comments": "off",
      "strings": "off"
    },
    "editor.suggestOnTriggerCharacters": false,
    "editor.inlineSuggest.enabled": false,
    "editor.wordBasedSuggestions": "off",
    "editor.parameterHints.enabled": false
  }
}
```

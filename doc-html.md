# Guia de HTML com Django

Este guia apresenta o essencial de HTML e mostra como usá-lo com Django:
requisição → URL → view → template HTML → resposta ao navegador.

## Índice

Use este índice como um dicionário: procure o assunto e abra o link para ir
direto à explicação.

### 🟢 HTML básico

- [1. O que é HTML?](#1-o-que-é-html)
- [2. Estrutura básica de uma página](#2-estrutura-básica-de-uma-página)
- [Abreviações Emmet no VS Code](#abreviações-emmet-no-vs-code)

### 🔵 Tags e elementos HTML

- [3. Tags HTML mais usadas](#3-tags-html-mais-usadas)
  - [Títulos e texto](#títulos-e-texto)
  - [Elementos semânticos de página](#elementos-semânticos-de-página)
  - [Agrupamento: `div`, `span`, `class` e `id`](#agrupamento)
  - [Listas](#listas)
  - [Tabelas](#tabelas)
- [5. Atributos HTML](#5-atributos-html)
- [14. Tags HTML de mídia e recursos](#14-tags-html-de-mídia-e-recursos)

### 🟣 Navegação, botões e conteúdo

- [4. Links, caminhos e imagens](#4-links-caminhos-e-imagens)
  - [Links](#links)
  - [Botões: navegar ou executar uma ação](#botões-navegar-ou-executar-uma-ação)
    - [Levar para outra página](#levar-para-outra-página)
    - [Criar um botão de ação](#criar-um-botão-de-ação)
    - [Estilizar o link como botão](#estilizar-o-link-como-botão)
  - [Imagens](#imagens)

### 🟠 Formulários

- [6. Formulários HTML](#6-formulários)
  - [Tipos de `input` frequentes](#tipos-de-input-frequentes)
- [9. Formulários com Django](#9-formulários-com-django)
- [19. Forms e ModelForms](#19-forms-e-modelforms)

### 🔴 Django: URLs, views e templates

- [7. HTML que conversa com Django](#7-html-que-conversa-com-django)
  - [7.1 Preparar o app e os templates](#71-preparar-o-app-e-os-templates)
  - [7.2 Ligar as URLs do projeto às URLs do app](#72-ligar-as-urls-do-projeto-às-urls-do-app)
  - [7.3 Criar uma view que renderiza HTML](#73-criar-uma-view-que-renderiza-html)
  - [7.4 Usar dados da view no template](#74-usar-dados-da-view-no-template)
- [8. Como o Django entrega uma página](#8-como-o-django-entrega-uma-página)
- [10. Sintaxe de templates Django](#10-sintaxe-de-templates-django)
  - [Condições e repetições](#condições-e-repetições)
  - [Filtros](#filtros)
- [11. Reutilizar o layout com `extends` e `block`](#11-reutilizar-o-layout-com-extends-e-block)
- [12. Usar nomes de URL nos links](#12-usar-nomes-de-url-nos-links)
- [18. Models e banco de dados](#18-models-e-banco-de-dados)
  - [Criar um model](#criar-um-model)
  - [Criar e aplicar migrações](#criar-e-aplicar-migrações)
- [20. CRUD: listar, visualizar, criar, editar e apagar](#20-crud-listar-visualizar-criar-editar-e-apagar)
- [21. Mensagens e redirecionamentos](#21-mensagens-e-redirecionamentos)
- [22. Login, logout e páginas protegidas](#22-login-logout-e-páginas-protegidas)
- [23. Upload e exibição de imagens](#23-upload-e-exibição-de-imagens)

### 🟡 Estilo, acessibilidade e solução de problemas

- [13. CSS e arquivos estáticos](#13-css-e-arquivos-estáticos)
- [15. Acessibilidade e boas práticas](#15-acessibilidade-e-boas-práticas)
- [16. Problemas comuns](#16-problemas-comuns)
- [24. Resumo: quem faz o quê?](#24-resumo-quem-faz-o-quê)

---

## 1. O que é HTML?

HTML significa *HyperText Markup Language*. É uma linguagem de marcação que
organiza o conteúdo de uma página. HTML define a estrutura; CSS cuida da
aparência; JavaScript pode adicionar interatividade. No Django, uma view
normalmente escolhe um template HTML e envia dados para ele.

Uma **tag** marca o início ou o fim de um elemento. Por exemplo,
`<p>Texto</p>` cria um parágrafo. A maioria dos elementos tem abertura e
fechamento; alguns, como `<img>` e `<input>`, não envolvem conteúdo.

## 2. Estrutura básica de uma página

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Minhas receitas</title>
</head>
<body>
  <header>
    <h1>Minhas receitas</h1>
  </header>

  <main>
    <p>Bem-vindo ao meu site!</p>
  </main>

  <footer>
    <p>Feito para aprender HTML e Django.</p>
  </footer>
</body>
</html>
```

- `<!DOCTYPE html>` declara um documento HTML moderno.
- `<html lang="pt-BR">` envolve a página e informa seu idioma.
- `<head>` contém informações sobre a página, não o conteúdo principal.
- `<meta charset="UTF-8">` permite representar caracteres como `ç` e `ã`.
- A meta tag `viewport` ajuda o layout a se adaptar a telas pequenas.
- `<title>` define o texto exibido na aba do navegador.
- `<body>` contém o conteúdo apresentado na página.

### Abreviações Emmet no VS Code

O VS Code inclui o **Emmet**, que transforma abreviações em trechos de HTML.
Por exemplo, `!` gera a estrutura inicial de uma página HTML, também chamada
de *boilerplate*.

Para usar:

1. Abra ou crie um arquivo com extensão `.html`.
2. Digite `!` em uma linha vazia.
3. Escolha a sugestão do Emmet e pressione `Tab` ou `Enter` para expandi-la.

Uma estrutura típica gerada por `!` é:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

Depois, ajuste o idioma, o título e o conteúdo, por exemplo, troque
`lang="en"` por `lang="pt-BR"` e o título `Document` pelo nome da página.
Essa abreviação cria apenas a estrutura do documento; ela não cria views,
rotas ou templates do Django.

Outras abreviações úteis:

| Abreviação | Resultado aproximado |
|---|---|
| `p` | `<p></p>` |
| `h1` | `<h1></h1>` |
| `a` | `<a href=""></a>` |
| `ul>li*3` | Uma lista `<ul>` com três itens `<li>` |
| `div.container` | `<div class="container"></div>` |
| `form>label+input+button` | Um formulário com label, campo e botão |

O Emmet funciona em arquivos HTML e também costuma funcionar em templates
Django (`.html`). Se a sugestão não aparecer, confira se o arquivo está sendo
reconhecido como HTML e abra as sugestões com `Ctrl+Space`.

## 3. Tags HTML mais usadas

### Títulos e texto

```html
<h1>Título principal</h1>
<h2>Seção</h2>
<h3>Subseção</h3>
<p>Um parágrafo de texto.</p>
<strong>Texto importante</strong>
<em>Texto enfatizado</em>
<br>
<hr>
```

- Use títulos de `<h1>` a `<h6>` em ordem lógica. Eles representam níveis de
  seção, não tamanhos que devem ser escolhidos só pela aparência.
- `<p>` representa um parágrafo.
- `<strong>` indica importância; `<em>` indica ênfase.
- `<br>` quebra uma linha e `<hr>` marca uma mudança temática. Não os use
  apenas para criar espaçamento visual; use CSS para isso.

### Elementos semânticos de página

```html
<header>Topo da página ou de uma seção</header>
<nav>Links de navegação</nav>
<main>Conteúdo principal da página</main>
<section>Seção temática</section>
<article>Conteúdo independente, como uma receita</article>
<aside>Conteúdo relacionado ou complementar</aside>
<footer>Rodapé da página ou de uma seção</footer>
```

Elementos semânticos descrevem o propósito do conteúdo e ajudam navegadores,
tecnologias assistivas e pessoas a entender a organização da página.

### Agrupamento

- `<div>` é um contêiner genérico em bloco. Use quando não houver um elemento
  semântico mais adequado.
- `<span>` é um contêiner genérico em linha, útil para marcar uma parte pequena
  do texto.
- `class` identifica um ou mais elementos para CSS e JavaScript.
- `id` identifica um elemento específico na página; cada `id` deve ser único.

```html
<section class="cartao-receita" id="bolo-de-cenoura">
  <h2>Bolo de cenoura</h2>
  <p>Uma receita <span class="destaque">simples</span>.</p>
</section>
```

### Listas

Lista sem ordem:

```html
<ul>
  <li>Farinha</li>
  <li>Leite</li>
  <li>Ovos</li>
</ul>
```

Lista ordenada:

```html
<ol>
  <li>Misture os ingredientes.</li>
  <li>Asse até dourar.</li>
</ol>
```

`<ul>` cria uma lista com marcadores, `<ol>` uma lista numerada e `<li>` cada
item da lista.

### Tabelas

Use tabelas para dados tabulares, não para organizar o layout da página.

```html
<table>
  <caption>Tempo de preparo das receitas</caption>
  <thead>
    <tr>
      <th scope="col">Receita</th>
      <th scope="col">Minutos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bolo de cenoura</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
```

- `<table>` cria a tabela; `<tr>` cria uma linha.
- `<th>` é uma célula de cabeçalho; `<td>` é uma célula de dados.
- `<thead>` e `<tbody>` agrupam cabeçalho e conteúdo.
- `<caption>` dá um título à tabela; `scope` ajuda a identificar o cabeçalho.

## 4. Links, caminhos e imagens

### Links

```html
<a href="/sobre/">Conheça o projeto</a>
<a href="https://www.djangoproject.com/">Site do Django</a>
<a href="#ingredientes">Ir para ingredientes</a>
```

`<a>` cria um link e `href` indica o destino. Para abrir uma nova aba, pode-se
usar `target="_blank"`; nesse caso, inclua também
`rel="noopener noreferrer"`.

### Botões: navegar ou executar uma ação

Use um link (`<a>`) para levar a pessoa a outra página. Use um botão (`<button>`)
para executar uma ação, como enviar um formulário. Embora seja possível
estilizar um link para parecer um botão, mantenha o elemento correto para a
função desejada.

#### Levar para outra página

Em um template Django, use um link com a tag `{% url %}` e uma classe CSS para
dar aparência de botão:

```django
<a class="botao" href="{% url 'sobre' %}">Conheça o projeto</a>
```

O nome `'sobre'` deve existir na configuração de URLs do app. Por exemplo, em
`recipes/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('sobre/', views.sobre, name='sobre'),
]
```

Django transforma o nome da rota no endereço correto. Assim, se o caminho
mudar, o template não precisa ser alterado. Para navegar até uma URL externa,
use o endereço diretamente:

```html
<a class="botao" href="https://www.djangoproject.com/">Documentação Django</a>
```

#### Criar um botão de ação

Use `<button>` dentro de um formulário quando a ação for enviar os dados:

```django
<form method="post">
  {% csrf_token %}
  <label for="nome">Seu nome</label>
  <input id="nome" name="nome" type="text" required>
  <button type="submit">Enviar</button>
</form>
```

`type="submit"` envia o formulário para a view que atende a página. Para um
botão que não deve enviar o formulário, declare `type="button"`:

```html
<button type="button">Abrir painel</button>
```

Esse botão sozinho não navega nem executa uma ação; normalmente ele é conectado
a JavaScript. Dentro de um formulário, não deixe o tipo implícito: um botão
sem `type` pode enviar o formulário.

#### Estilizar o link como botão

Adicione uma classe ao link:

```html
<a class="botao" href="/sobre/">Sobre</a>
```

E defina a aparência no CSS:

```css
.botao {
  display: inline-block;
  padding: 0.6rem 1rem;
  border-radius: 0.3rem;
  background-color: #2457a7;
  color: white;
  text-decoration: none;
}

.botao:hover {
  background-color: #183d78;
}
```

O elemento continua sendo um link: teclado e tecnologias assistivas sabem que
ele navega para outra página. Para uma ação de formulário, use `<button>` e
estilize o botão diretamente.

### Imagens

```html
<img src="/static/recipes/img/bolo.jpg" alt="Bolo de cenoura com cobertura">
```

`src` indica onde está a imagem. `alt` descreve a imagem para quem não consegue
vê-la e é importante para acessibilidade. Se a imagem for apenas decorativa,
use `alt=""`.

No Django, prefira gerar caminhos de arquivos estáticos com a tag `{% static %}`;
veja a seção [CSS e arquivos estáticos](#13-css-e-arquivos-estáticos).

## 5. Atributos HTML

Atributos acrescentam informações a uma tag e aparecem na tag de abertura:

```html
<input type="text" name="nome" id="nome" placeholder="Seu nome" required>
```

Atributos comuns:

- `class`: uma ou mais classes para estilização ou seleção.
- `id`: identificador único.
- `href`: destino de um link.
- `src`: origem de imagem, áudio, vídeo ou script externo.
- `alt`: texto alternativo de uma imagem.
- `name`: nome usado para enviar o valor de um campo de formulário.
- `value`: valor inicial ou enviado de um campo.
- `type`: tipo de campo ou botão.
- `placeholder`: dica visual dentro de um campo; não substitui um `<label>`.
- `required`, `disabled`, `checked`: atributos booleanos para controles.

Os valores de atributos devem ficar entre aspas. Use nomes claros e evite
repetir o mesmo `id` em mais de um elemento.

## 6. Formulários

Formulários coletam dados e os enviam ao servidor. Cada campo precisa de um
`name` para que seu valor seja enviado.

```html
<form action="/contato/" method="post">
  <label for="nome">Nome</label>
  <input id="nome" name="nome" type="text" required>

  <label for="email">E-mail</label>
  <input id="email" name="email" type="email" required>

  <label for="mensagem">Mensagem</label>
  <textarea id="mensagem" name="mensagem" rows="5" required></textarea>

  <button type="submit">Enviar</button>
</form>
```

- `<form>` agrupa os campos e define destino (`action`) e método (`method`).
- `<label for="...">` associa um rótulo ao campo que tem o mesmo `id`.
- `<input>` cria campos de entrada; `<textarea>` permite texto maior.
- `<button type="submit">` envia o formulário.
- `required` pede ao navegador que o campo seja preenchido; o servidor também
  deve validar os dados.

### Tipos de `input` frequentes

```html
<input type="text" name="nome">
<input type="email" name="email">
<input type="password" name="senha">
<input type="number" name="quantidade" min="1">
<input type="date" name="data">
<input type="checkbox" name="vegetariana">
<input type="radio" name="tamanho" value="pequena">
<input type="file" name="foto">
<input type="search" name="busca">
```

Outros elementos úteis:

- `<select name="categoria">` com opções `<option value="...">`.
- `<textarea name="comentario"></textarea>` para texto com várias linhas.
- `<button type="button">` para um botão que não envia o formulário.
- `<button type="reset">` restaura os valores iniciais do formulário.

Para enviar arquivos, o formulário precisa de
`enctype="multipart/form-data"` e a view deve tratar `request.FILES`.

## 7. HTML que conversa com Django

O navegador envia uma requisição para uma URL. O Django encontra a rota, chama
uma view e a view retorna uma resposta. Quando essa resposta é uma página,
normalmente a view renderiza um template.

```text
Navegador → projeto/urls.py → recipes/urls.py → view → template HTML → navegador
```

### 7.1 Preparar o app e os templates

Confirme que o app está registrado em `INSTALLED_APPS`, no arquivo
`projeto/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'recipes.apps.RecipesConfig',
]
```

Com `APP_DIRS = True` nas configurações de templates do projeto, uma estrutura
comum é guardar os templates dentro do app:

```text
recipes/
├── templates/
│   └── recipes/
│       ├── base.html
│       ├── home.html
│       └── contato.html
├── urls.py
└── views.py
```

O subdiretório `templates/recipes/` evita conflitos quando diferentes apps
têm templates com nomes iguais.

### 7.2 Ligar as URLs do projeto às URLs do app

No arquivo `projeto/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
```

No arquivo `recipes/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
```

`include('recipes.urls')` encaminha as rotas para o app. O primeiro argumento
de `path()` é o caminho; o segundo é a view. `name` dá um nome estável à rota,
que pode ser usado nos templates com `{% url %}`.

Com esse exemplo, as páginas ficam em `/`, `/sobre/` e `/contato/`.

### 7.3 Criar uma view que renderiza HTML

No arquivo `recipes/views.py`:

```python
from django.shortcuts import render


def home(request):
    contexto = {
        'titulo': 'Receitas da casa',
        'receitas': ['Bolo de cenoura', 'Pão de queijo'],
    }
    return render(request, 'recipes/home.html', contexto)
```

- `request` representa a requisição que chegou ao Django.
- `render()` combina a requisição, o template e um dicionário de dados
  (`contexto`) e devolve uma resposta HTTP.
- O template recebe os valores do dicionário pelas respectivas chaves.

`HttpResponse` também pode devolver uma resposta diretamente, por exemplo
`return HttpResponse('Olá!')`, mas templates são mais apropriados para páginas
HTML maiores.

### 7.4 Usar dados da view no template

No arquivo `recipes/templates/recipes/home.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{{ titulo }}</title>
</head>
<body>
  <h1>{{ titulo }}</h1>

  <ul>
    {% for receita in receitas %}
      <li>{{ receita }}</li>
    {% empty %}
      <li>Nenhuma receita cadastrada.</li>
    {% endfor %}
  </ul>
</body>
</html>
```

`{{ titulo }}` exibe um valor. `{% for %}` percorre a lista recebida pela view;
`{% empty %}` mostra uma alternativa quando a lista não tem itens.

## 8. Como o Django entrega uma página

Este é o caminho completo para abrir a página inicial:

1. A pessoa acessa `/` no navegador.
2. `projeto/urls.py` inclui `recipes.urls`.
3. `recipes/urls.py` encontra a rota `''` e chama `views.home`.
4. `home(request)` prepara dados e chama `render()`.
5. Django processa o template e substitui as variáveis.
6. O navegador recebe e interpreta o HTML.

Uma view não é o próprio arquivo HTML: ela é código Python que decide como
responder. Um template não é uma view: é um arquivo que descreve a estrutura
apresentada ao navegador.

## 9. Formulários com Django

Em formulários que alteram ou enviam dados, use `method="post"` e a tag
`{% csrf_token %}` dentro do formulário. O token protege a requisição contra
ataques CSRF.

Template `recipes/templates/recipes/contato.html`:

```html
<h1>Contato</h1>

{% if enviado %}
  <p>Obrigado pela mensagem, {{ nome }}!</p>
{% else %}
  <form method="post">
    {% csrf_token %}

    <label for="nome">Nome</label>
    <input id="nome" name="nome" type="text" required>

    <label for="mensagem">Mensagem</label>
    <textarea id="mensagem" name="mensagem" required></textarea>

    <button type="submit">Enviar</button>
  </form>
{% endif %}
```

View simplificada em `recipes/views.py`:

```python
from django.shortcuts import render


def contato(request):
    contexto = {'enviado': False, 'nome': ''}

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        mensagem = request.POST.get('mensagem', '').strip()
        contexto['nome'] = nome
        contexto['enviado'] = bool(nome and mensagem)

    return render(request, 'recipes/contato.html', contexto)
```

`request.method` informa o método HTTP usado. Campos enviados por POST são
acessados com `request.POST.get('nome')`. Esse exemplo apenas verifica se os
campos têm conteúdo; um formulário real também precisa de validação adequada
e de uma ação definida para salvar ou encaminhar a mensagem.

Use GET para buscas que não alteram dados; valores GET aparecem na URL e são
acessados com `request.GET`. Não envie senhas ou informações privadas em
parâmetros GET.

## 10. Sintaxe de templates Django

Templates Django usam três construções principais:

- `{{ variavel }}` exibe um valor, como `{{ receita.nome }}`.
- `{% tag %}` executa uma instrução de template, como `{% if usuario %}`.
- `{# comentário #}` adiciona um comentário que não aparece no HTML gerado.

### Condições e repetições

```django
{% if receitas %}
  <p>Há receitas disponíveis.</p>
{% elif carregando %}
  <p>Carregando...</p>
{% else %}
  <p>Nenhuma receita encontrada.</p>
{% endif %}

{% for receita in receitas %}
  <h2>{{ receita.nome }}</h2>
{% empty %}
  <p>A lista está vazia.</p>
{% endfor %}
```

Dentro de um `for`, `forloop.counter` começa em 1 e `forloop.counter0` começa
em 0. Outros valores úteis incluem `forloop.first` e `forloop.last`.

### Filtros

Filtros transformam valores e são escritos depois de `|`:

```django
{{ nome|title }}
{{ descricao|truncatewords:20 }}
{{ receitas|length }}
{{ mensagem|default:"Sem mensagem" }}
```

Filtros comuns:

- `lower` e `upper`: convertem o texto para minúsculas ou maiúsculas.
- `title` e `capfirst`: colocam palavras em formato de título ou capitalizam
  a primeira letra.
- `length`: retorna o tamanho de um texto ou lista.
- `default:"valor"`: mostra um valor alternativo quando o valor é vazio.
- `date:"d/m/Y"`: formata uma data.
- `truncatewords:20`: limita o texto a uma quantidade de palavras.
- `join:", "`: une os itens de uma lista usando o separador indicado.

Por segurança, Django escapa automaticamente HTML inserido em variáveis nos
templates. Evite o filtro `safe` a menos que você tenha certeza de que o
conteúdo é confiável e foi sanitizado.

## 11. Reutilizar o layout com `extends` e `block`

Um layout base evita repetir cabeçalho, navegação e rodapé em cada página.

`recipes/templates/recipes/base.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block titulo %}Meu site{% endblock %}</title>
</head>
<body>
  <header>
    <nav>
      <a href="{% url 'home' %}">Início</a>
      <a href="{% url 'sobre' %}">Sobre</a>
      <a href="{% url 'contato' %}">Contato</a>
    </nav>
  </header>

  <main>
    {% block conteudo %}{% endblock %}
  </main>
</body>
</html>
```

`recipes/templates/recipes/home.html`:

```django
{% extends "recipes/base.html" %}

{% block titulo %}Início | Meu site{% endblock %}

{% block conteudo %}
  <h1>{{ titulo }}</h1>
  <p>Bem-vindo!</p>
{% endblock %}
```

`{% extends %}` herda o layout. Cada `{% block %}` define uma área que um
template filho pode substituir.

## 12. Usar nomes de URL nos links

Prefira `{% url %}` a escrever caminhos manualmente:

```django
<a href="{% url 'home' %}">Início</a>
<a href="{% url 'contato' %}">Fale conosco</a>
```

Os nomes precisam corresponder ao argumento `name` no `path()` de
`recipes/urls.py`. Assim, se o caminho mudar, os links continuam funcionando
sem precisar atualizar cada template.

## 13. CSS e arquivos estáticos

CSS, imagens e JavaScript do projeto são arquivos estáticos. Uma estrutura
comum dentro do app:

```text
recipes/
├── static/
│   └── recipes/
│       ├── css/
│       │   └── estilo.css
│       └── img/
│           └── logo.png
└── templates/
    └── recipes/
        └── base.html
```

No início do template, carregue a tag `static` e use-a para montar o caminho:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'recipes/css/estilo.css' %}">
<img src="{% static 'recipes/img/logo.png' %}" alt="Logo do site">
```

Exemplo de `recipes/static/recipes/css/estilo.css`:

```css
body {
  font-family: sans-serif;
  line-height: 1.5;
  margin: 2rem auto;
  max-width: 60rem;
  padding: 0 1rem;
}

.destaque {
  color: #8b2f2f;
}
```

Em desenvolvimento, `DEBUG=True` e `django.contrib.staticfiles` permitem que
Django sirva arquivos estáticos no fluxo usual de desenvolvimento. Em produção,
configure a coleta e o servidor de arquivos estáticos conforme o ambiente.

## 14. Tags HTML de mídia e recursos

```html
<audio controls src="/static/recipes/audio/intro.mp3">
  Seu navegador não oferece suporte a áudio.
</audio>

<video controls width="640">
  <source src="/static/recipes/video/preparo.mp4" type="video/mp4">
  Seu navegador não oferece suporte a vídeo.
</video>

<iframe
  src="https://www.example.com"
  title="Conteúdo externo"
  loading="lazy">
</iframe>
```

- `<audio>` e `<video>` incorporam mídia; `controls` exibe controles.
- `<source>` oferece uma fonte de mídia.
- `<iframe>` incorpora outra página. Use um `title` descritivo e incorpore
  conteúdo externo somente quando necessário e confiável.

## 15. Acessibilidade e boas práticas

- Use elementos semânticos (`<main>`, `<nav>`, `<header>`, `<footer>`) quando
  forem apropriados.
- Associe cada campo de formulário a um `<label>`.
- Forneça `alt` útil para imagens informativas.
- Mantenha uma hierarquia coerente de títulos.
- Use texto de link que explique o destino; evite “clique aqui” sem contexto.
- Não use tabelas para layout.
- Não dependa apenas de cor para transmitir uma informação.
- Valide os dados no servidor; validação HTML melhora a experiência, mas pode
  ser contornada.
- Não coloque senhas, chaves secretas ou dados privados no HTML.
- Não use `{% autoescape off %}` nem `|safe` para conteúdo de usuário.

## 16. Problemas comuns

**A página retorna erro de template não encontrado**

- Confira se o app está em `INSTALLED_APPS`.
- Com `APP_DIRS=True`, confirme o caminho
  `recipes/templates/recipes/nome-do-template.html`.
- Confira se o nome passado a `render()` corresponde ao caminho dentro de
  `templates/`, por exemplo `recipes/home.html`.

**O Django não encontra uma URL**

- Confira se `projeto/urls.py` inclui `recipes.urls`.
- Confira se o `path()` está em `urlpatterns` e se o caminho termina com a
  barra esperada.
- Se usar `{% url 'home' %}`, confirme que a rota tem `name='home'`.

**O formulário POST retorna erro CSRF**

- Inclua `{% csrf_token %}` dentro de cada formulário POST renderizado pelo
  Django.
- Não remova a proteção CSRF para resolver o erro.

**O CSS ou a imagem não aparece**

- Confira se o arquivo está dentro de `static/` no caminho esperado.
- Confira `{% load static %}` e o caminho passado a `{% static %}`.
- Verifique se o nome e as letras maiúsculas/minúsculas correspondem ao arquivo.

**A tabela do banco não existe**

- Confira se o model está salvo em `models.py`.
- Rode `python manage.py makemigrations` e depois
  `python manage.py migrate`.
- Confira se o app está em `INSTALLED_APPS`.

**O nome de uma URL não foi encontrado**

- Confira o `name` no `path()` e, se existir `app_name`, use o namespace no
  template, como `{% url 'recipes:list' %}`.

**A imagem enviada não aparece**

- Arquivos enviados pelo usuário são mídia (`MEDIA_ROOT`/`MEDIA_URL`), não
  arquivos estáticos (`static/`). Confira a configuração da seção de upload.

## 18. Models e banco de dados

Um **model** descreve os dados que o Django guarda no banco. Cada atributo
normalmente representa uma coluna. O ORM do Django permite consultar e alterar
esses dados usando Python, sem escrever SQL para as operações comuns.

### Criar um model

Em `recipes/models.py`, defina, por exemplo, uma receita:

```python
from django.conf import settings
from django.db import models


class Receita(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='receitas',
    )
    imagem = models.ImageField(upload_to='receitas/', blank=True)

    class Meta:
        ordering = ['-criada_em']

    def __str__(self):
        return self.titulo
```

- `CharField` guarda texto curto e exige `max_length`.
- `TextField` guarda texto maior.
- `DateTimeField(auto_now_add=True)` grava a data/hora de criação.
- `ForeignKey` relaciona cada receita a um usuário. `CASCADE` significa que,
  ao apagar esse usuário, suas receitas também serão apagadas.
- `ImageField` guarda o caminho do arquivo enviado, não a imagem dentro da
  tabela. Para usá-lo, instale a dependência Pillow com
  `python -m pip install Pillow`.
- `__str__()` define uma representação legível do objeto.

O exemplo associa receitas a usuários para que cada pessoa possa gerenciar as
próprias receitas. Se o projeto ainda não tiver autenticação, pode-se começar
com outro modelo sem `autor`, mas as operações de criação e edição abaixo usam
login e autoria.

Para ver o model no painel administrativo, registre-o em `recipes/admin.py`:

```python
from django.contrib import admin
from .models import Receita

admin.site.register(Receita)
```

### Criar e aplicar migrações

Migrações são instruções versionadas que sincronizam os models com a estrutura
do banco. Depois de criar ou alterar um model, execute na pasta de `manage.py`:

```bash
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations` cria arquivos de migração a partir das mudanças nos models.
- `migrate` aplica as migrações pendentes ao banco configurado.
- Ao alterar models no futuro, repita os dois comandos e inclua os arquivos de
  migração no controle de versão.

Para consultar dados no shell interativo do Django:

```bash
python manage.py shell
```

```python
from recipes.models import Receita

Receita.objects.all()
Receita.objects.filter(titulo__icontains='bolo')
```

## 19. Forms e ModelForms

Um `Form` ou `ModelForm` valida os dados recebidos e ajuda a gerar os campos
HTML. `ModelForm` é útil quando o formulário cria ou atualiza um model.
Validação no navegador (`required`, por exemplo) melhora a experiência, mas
não substitui validação no servidor.

Use `forms.Form` quando os dados não precisarem ser salvos diretamente em um
model. Por exemplo, em `recipes/forms.py`:

```python
from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
```

Na view, faça a validação no POST:

```python
if request.method == 'POST':
    form = ContatoForm(request.POST)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['mensagem']
else:
    form = ContatoForm()
```

`is_valid()` verifica os campos; `cleaned_data` contém os valores já validados.
Use esses valores para processar a mensagem ou executar outra ação.

Em `recipes/forms.py`, crie um formulário baseado no model:

```python
from django import forms
from .models import Receita


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'descricao', 'imagem']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }
```

Inclua somente os campos que a pessoa pode editar. Não inclua `autor`: a view
deve atribuir o usuário autenticado, em vez de aceitar essa informação do
navegador.

Template `recipes/templates/recipes/receita_form.html`:

```django
<h1>{{ titulo_pagina }}</h1>

<form method="post" enctype="multipart/form-data">
  {% csrf_token %}

  {{ form.non_field_errors }}

  {% for field in form %}
    <div>
      {{ field.label_tag }}
      {{ field }}
      {{ field.errors }}
    </div>
  {% endfor %}

  <button type="submit">Salvar</button>
</form>
```

- `form.non_field_errors` mostra erros que não pertencem a um campo específico.
- `field.errors` mostra erros daquele campo.
- `enctype="multipart/form-data"` é necessário para enviar arquivos.
- `{% csrf_token %}` protege o formulário POST.

O método `form.is_valid()` executa a validação. Os erros ficam disponíveis no
formulário para serem mostrados no template.

## 20. CRUD: listar, visualizar, criar, editar e apagar

CRUD é a sigla de *Create, Read, Update, Delete*: criar, ler, atualizar e
apagar dados. Os exemplos usam o model `Receita`, o formulário `ReceitaForm`
e as rotas com namespace definidos nesta documentação. As views exigem login;
veja também a seção [Login, logout e páginas protegidas](#22-login-logout-e-páginas-protegidas).

Em `recipes/views.py`:

```python
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReceitaForm
from .models import Receita


@login_required
def receita_lista(request):
    receitas = Receita.objects.filter(autor=request.user)
    return render(request, 'recipes/receita_lista.html', {
        'receitas': receitas,
    })


@login_required
def receita_detalhe(request, pk):
    receita = get_object_or_404(Receita, pk=pk, autor=request.user)
    return render(request, 'recipes/receita_detalhe.html', {
        'receita': receita,
    })


@login_required
def receita_criar(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user
            receita.save()
            messages.success(request, 'Receita criada com sucesso.')
            return redirect('recipes:detalhe', pk=receita.pk)
    else:
        form = ReceitaForm()

    return render(request, 'recipes/receita_form.html', {
        'form': form,
        'titulo_pagina': 'Criar receita',
    })


@login_required
def receita_editar(request, pk):
    receita = get_object_or_404(Receita, pk=pk, autor=request.user)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES, instance=receita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita atualizada com sucesso.')
            return redirect('recipes:detalhe', pk=receita.pk)
    else:
        form = ReceitaForm(instance=receita)

    return render(request, 'recipes/receita_form.html', {
        'form': form,
        'titulo_pagina': 'Editar receita',
    })


@login_required
def receita_apagar(request, pk):
    receita = get_object_or_404(Receita, pk=pk, autor=request.user)
    if request.method == 'POST':
        receita.delete()
        messages.success(request, 'Receita apagada com sucesso.')
        return redirect('recipes:lista')

    return render(request, 'recipes/receita_confirmar_apagar.html', {
        'receita': receita,
    })
```

O filtro `autor=request.user` é importante: impede que uma pessoa veja, edite
ou apague uma receita pertencente a outro usuário, mesmo que tente adivinhar
seu identificador (`pk`).

Em `recipes/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('receitas/', views.receita_lista, name='lista'),
    path('receitas/nova/', views.receita_criar, name='criar'),
    path('receitas/<int:pk>/', views.receita_detalhe, name='detalhe'),
    path('receitas/<int:pk>/editar/', views.receita_editar, name='editar'),
    path('receitas/<int:pk>/apagar/', views.receita_apagar, name='apagar'),
]
```

O `app_name` cria um namespace; por isso, links e redirecionamentos usam nomes
como `'recipes:lista'`. `<int:pk>` captura um número da URL e o envia à view.

Exemplo de listagem, em `recipes/templates/recipes/receita_lista.html`:

```django
<h1>Minhas receitas</h1>
<a href="{% url 'recipes:criar' %}">Nova receita</a>

{% for receita in receitas %}
  <article>
    <h2>
      <a href="{% url 'recipes:detalhe' receita.pk %}">
        {{ receita.titulo }}
      </a>
    </h2>
    <p>{{ receita.descricao|truncatewords:20 }}</p>
    <a href="{% url 'recipes:editar' receita.pk %}">Editar</a>
    <a href="{% url 'recipes:apagar' receita.pk %}">Apagar</a>
  </article>
{% empty %}
  <p>Você ainda não cadastrou receitas.</p>
{% endfor %}
```

Exemplo de detalhe, em `recipes/templates/recipes/receita_detalhe.html`:

```django
<h1>{{ receita.titulo }}</h1>
<p>{{ receita.descricao|linebreaks }}</p>

{% if receita.imagem %}
  <img src="{{ receita.imagem.url }}" alt="Imagem de {{ receita.titulo }}">
{% endif %}

<a href="{% url 'recipes:editar' receita.pk %}">Editar</a>
<a href="{% url 'recipes:lista' %}">Voltar às receitas</a>
```

Apagar dados deve usar POST, não um link GET. Template de confirmação,
`recipes/templates/recipes/receita_confirmar_apagar.html`:

```django
<h1>Apagar receita?</h1>
<p>Confirma apagar "{{ receita.titulo }}"?</p>

<form method="post">
  {% csrf_token %}
  <button type="submit">Sim, apagar</button>
</form>

<a href="{% url 'recipes:detalhe' receita.pk %}">Cancelar</a>
```

Para editar e apagar, sempre busque o objeto com o usuário atual como parte do
filtro. Não confie apenas em esconder botões no template: a autorização precisa
ser verificada também na view.

## 21. Mensagens e redirecionamentos

O framework de mensagens do Django permite apresentar avisos após uma ação.
O middleware e o context processor de mensagens já vêm habilitados na
configuração padrão criada pelo Django.

Na view, importe e use uma categoria apropriada:

```python
from django.contrib import messages
from django.shortcuts import redirect

messages.success(request, 'Alterações salvas.')
messages.error(request, 'Não foi possível salvar.')
return redirect('recipes:lista')
```

Outras categorias incluem `info`, `warning` e `debug`. Exiba as mensagens uma
única vez em um template compartilhado, por exemplo dentro do `<main>` de
`base.html`:

```django
{% if messages %}
  <ul class="mensagens">
    {% for message in messages %}
      <li class="{{ message.tags }}">{{ message }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

Depois de processar com sucesso um POST, redirecione para outra página. Esse
padrão evita que atualizar o navegador envie novamente o formulário. O
redirecionamento pode usar um nome de URL (`redirect('recipes:lista')`) ou um
objeto (`redirect('recipes:detalhe', pk=receita.pk)`).

## 22. Login, logout e páginas protegidas

Django inclui views de autenticação para login, logout e recuperação de senha.
Não implemente armazenamento ou comparação manual de senhas; use o sistema de
autenticação do Django, que aplica o tratamento seguro apropriado.

Inclua as rotas de autenticação em `projeto/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('recipes.urls')),
]
```

As views padrão usam templates no diretório `registration/`. Crie
`recipes/templates/registration/login.html` (o mecanismo de templates encontra
esse caminho porque `APP_DIRS=True` e o app está instalado):

```django
<h1>Entrar</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Entrar</button>
</form>
```

Configure destinos após login e logout em `projeto/settings.py`:

```python
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/receitas/'
LOGOUT_REDIRECT_URL = '/'
```

Proteja views que exigem autenticação:

```python
from django.contrib.auth.decorators import login_required


@login_required
def area_privada(request):
    return render(request, 'recipes/privada.html')
```

O decorator redireciona visitantes não autenticados para a página de login.
Para views baseadas em classes, existe `LoginRequiredMixin`.

Em templates, `user` fica disponível pela configuração padrão:

```django
{% if user.is_authenticated %}
  <p>Olá, {{ user.username }}.</p>
  <form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Sair</button>
  </form>
{% else %}
  <a href="{% url 'login' %}">Entrar</a>
{% endif %}
```

Para criar usuários de teste ou um administrador, use o comando
`python manage.py createsuperuser` ou o fluxo de cadastro implementado com
formulários próprios do Django. Não aceite que o formulário escolha quais
permissões administrativas um usuário recebe.

## 23. Upload e exibição de imagens

Uploads enviados por usuários são **arquivos de mídia**. Diferem de arquivos
estáticos: o CSS e os ícones do site pertencem a `static/`; imagens de receitas
enviadas por pessoas pertencem a `MEDIA_ROOT`.

Para o `ImageField` do model, instale Pillow:

```bash
python -m pip install Pillow
```

Configure `projeto/settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Sirva mídia localmente apenas durante o desenvolvimento, em `projeto/urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

No formulário, use `enctype="multipart/form-data"`. Na view, passe ambos os
conjuntos de dados:

```python
form = ReceitaForm(request.POST, request.FILES)
```

Para exibir uma imagem já enviada:

```django
{% if receita.imagem %}
  <img src="{{ receita.imagem.url }}" alt="Imagem de {{ receita.titulo }}">
{% endif %}
```

O arquivo é gravado em `MEDIA_ROOT/receitas/`, conforme `upload_to`. A URL é
montada usando `MEDIA_URL`.

**Cuidados com uploads:** limite tamanho e tipos permitidos, valide o conteúdo
no servidor e não confie apenas na extensão ou no `Content-Type` enviado pelo
navegador. Arquivos enviados por usuários não devem ser executados como código.
A configuração acima é para desenvolvimento; em produção, use armazenamento e
servidor de mídia apropriados e siga a configuração do ambiente.

## 24. Resumo: quem faz o quê?

| Parte | Responsabilidade |
|---|---|
| HTML | Estrutura e conteúdo da página |
| CSS | Aparência e layout |
| URL (`urls.py`) | Associa um caminho a uma view |
| View (`views.py`) | Processa a requisição e prepara a resposta |
| Template (`.html`) | Define a página e apresenta os dados |
| Contexto | Dados enviados pela view ao template |
| Model (`models.py`) | Descreve os dados armazenados no banco |
| Form/ModelForm | Valida dados enviados e gera controles de formulário |
| Migração | Registra e aplica mudanças na estrutura do banco |
| Tag Django | Instrução de template, como `if`, `for`, `url` ou `static` |
| Arquivo estático | CSS, JavaScript e imagens que fazem parte do site |
| Arquivo de mídia | Arquivo enviado pelo usuário, como uma foto de receita |

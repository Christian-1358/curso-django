"""
====================================================================
Script Demonstrativo Completo da Biblioteca Rich em Python 3
====================================================================
Este script reúne múltiplos componentes visuais e profissionais
para tornar a interface de linha de comandos (CLI) moderna e apelativa:
- Consola com cores e formatação rica
- Painéis estilizados (Panels)
- Tabelas dinâmicas
- Destaque de sintaxe de código (Syntax Highlighting)
- Indicadores de progresso e spinners
"""

from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from rich.progress import Progress, SpinnerColumn, TextColumn

# Inicializa a consola principal do Rich
console = Console()

def executar_demonstracao():
    # 1. Cabeçalho com Painel Estilizado
    console.print(Panel.fit(
        "[bold cyan]Painel de Demonstração Profissional - Rich[/bold cyan]\n"
        "[italic dim]Exemplos completos de componentes visuais para terminal[/italic dim]",
        title="[yellow]Sistema CLI Ativo[/yellow]",
        border_style="green"
    ))

    # 2. Demonstração de Texto Estilizado Inline
    console.print("\n[bold magenta]>> 1. Formatação de Texto Dinâmica[/bold magenta]")
    console.print("Podes misturar [red]cores[/red], [bold]negrito[/bold], [underline]sublinhado[/underline] e até [on blue]fundos personalizados[/on blue] de forma muito simples.")

    # 3. Demonstração de Tabelas Organizadas
    console.print("\n[bold magenta]>> 2. Tabelas de Dados Estruturadas[/bold magenta]")
    tabela = Table(title="Registo de Módulos do Sistema", title_style="bold cyan")
    
    # Adicionar colunas com alinhamentos e estilos
    tabela.add_column("ID", justify="center", style="yellow", no_wrap=True)
    tabela.add_column("Módulo", style="green")
    tabela.add_column("Estado", justify="right", style="bold magenta")

    # Adicionar linhas de dados
    tabela.add_row("01", "Autenticação de Utilizador", "[green]Ativo[/green]")
    tabela.add_row("02", "Conexão com Base de Dados", "[green]Ativo[/green]")
    tabela.add_row("03", "Motor de Processamento", "[yellow]Aviso[/yellow]")
    
    console.print(tabela)

    # 4. Demonstração de Destaque de Sintaxe (Syntax Highlighting)
    console.print("\n[bold magenta]>> 3. Destaque de Sintaxe de Código[/bold magenta]")
    codigo_exemplo = '''def calcular_imposto(valor, taxa):
    # Calcula o valor final com base na taxa aplicada
    total = valor + (valor * taxa)
    return round(total, 2)
'''
    # Cria o objeto de sintaxe formatado para Python
    sintaxe = Syntax(codigo_exemplo, "python", theme="monokai", line_numbers=True)
    console.print(sintaxe)

    # 5. Demonstração de Processamento com Spinner / Progresso
    console.print("\n[bold magenta]>> 4. Simulação de Tarefa em Segundo Plano[/bold magenta]")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progresso:
        # Adiciona uma tarefa de carregamento dinâmica
        progresso.add_task("[cyan]A sincronizar dados com o servidor...", total=None)
        sleep(2)  # Simula tempo de processamento

    # Mensagem de sucesso final
    console.print("[bold green]✔ Sincronização concluída com sucesso![/bold green]")

    # 6. Rodapé Final com Painel
    console.print("\n")
    console.print(Panel("[bold white]Execução finalizada com êxito. Todos os componentes responderam conforme esperado.[/bold white]", border_style="blue"))

if __name__ == "__main__":
    executar_demonstracao()
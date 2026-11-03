from rich.console import Console
from rich.panel import Panel

console = Console()

class Livro:
    def __init__(self, titulo, autor, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.paginas = paginas
        self.pagina_atual = 0  

    def mostrar_capa(self):
        conteudo = f"[bold cyan]Autor:[/bold cyan] {self.autor}\n[bold yellow]Ano:[/bold yellow] {self.ano}"
        console.print(Panel(conteudo, title=f"[bold green]{self.titulo}[/bold green]", expand=False))

    def passar_pagina(self):
        if self.pagina_atual < len(self.paginas):
            texto_pagina = self.paginas[self.pagina_atual]
            console.print(Panel(texto_pagina, title=f"Página {self.pagina_atual + 1}"))
            self.pagina_atual += 1
        else:
            console.print("[bold red]Você chegou ao fim da leitura![/bold red]")

conteudo_paginas = [
    "akaksadalhifhkfhskfshkffskljfshfjhsfnsfhsdfslfj",
    "fjodjldalkdajldajldjaldldjl",
    "lfjdlajdlajdlajlddlaj"
]

meu_livro = Livro("Doutor Nerfario", "Chris", 2000, conteudo_paginas)

# Exemplo de uso:
meu_livro.mostrar_capa()
meu_livro.passar_pagina()  # Vai para a página 1
meu_livro.passar_pagina()  # Vai para a página 2
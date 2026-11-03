
from rich.console import Console
from rich.panel import Panel
import rich

class Gamer:
    def __int__(self, nome, nick, jogos_favorito):
  
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favorito
        
    def mostrar_ficha(self):
        jogos_str = ", ".join(self.jogos_favoritos)
        conteudo = f"[bold cyan]Nome:[/bold cyan] {self.nome}\n" \
                   f"[bold green]Nick:[/bold green] {self.nick}\n" \
                   f"[bold yellow]Jogos Favoritos:[/bold yellow] {jogos_str}"
        
        rich.console.print(Panel(conteudo, title=f"🎮 Ficha Gamer - {self.nick}", expand=False))
        
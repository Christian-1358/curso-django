from rich.console import Console

console = Console()

class ControleRemoto:
    def __init__(self):
        # Estados iniciais do controle
        self.ligado = False
        self.canal = 1
        self.volume = 20

    def ligar_desligar(self):
        # Inverte o estado atual (se estiver desligado, liga; se estiver ligado, desliga)
        self.ligado = not self.ligado
        if self.ligado:
          console.print("[bold green]Televisão LIGADA![/bold green]")
        else:
          console.print("[bold red]Televisão DESLIGADA![/bold red]")

    def aumentar_volume(self):
        if self.ligado:
            self.volume += 1
            console.print(f"[cyan]Volume atual: {self.volume}[/cyan]")
        else:
            console.print("[red]A TV está desligada! Impossível alterar o volume.[/red]")

    def mudar_canal(self, novo_canal):
        if self.ligado:
            self.canal = novo_canal
            console.print(f"[yellow]Canal alterado para: {self.canal}[/yellow]")
        else:
            console.print("[red]A TV está desligada! Impossível mudar de canal.[/red]")

# Exemplo de uso:
# controle = ControleRemoto()
# controle.ligar_desligar()  # Liga a TV
# controle.aumentar_volume() # Aumenta o volume
# controle.mudar_canal(5)    # Muda para o canal 5

#nao suibe fazer
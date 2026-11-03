from abc import ABC, abstractmethod
import rich

class Personagem(ABC):
    def __init__(self, nome: str, vida: int = 100):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca: int):
        rich.print(f"[bold red]{self.nome}[/bold red] atacou [bold cyan]{alvo.nome}[/bold cyan] com força {forca}!")
        alvo.receber_dano(forca)

    def receber_dano(self, dano: int):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        rich.print(f"[yellow]{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}[/yellow]")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome: str, vida: int = 120):
        super().__init__(nome, vida)
        self.golpes = ["Espada Pesada", "Investida"]

    def curar(self):
        cura = 15
        self.vida += cura
        rich.print(f"[bold green]{self.nome} (Guerreiro) usou bandagem e recuperou {cura} de vida! Vida atual: {self.vida}[/bold green]")


class Mago(Personagem):
    def __init__(self, nome: str, vida: int = 80):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio Congelante"]

    def curar(self):
        cura = 25
        self.vida += cura
        rich.print(f"[bold green]{self.nome} (Mago) usou magia de cura e recuperou {cura} de vida! Vida atual: {self.vida}[/bold green]")


guerreiro = Guerreiro("Arthur")
mago = Mago("Merlin")

guerreiro.atacar(mago, 30)
mago.curar()
mago.atacar(guerreiro, 25)
guerreiro.curar()
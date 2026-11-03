from rich.console import Console

# Instância do console para imprimir com cores
console = Console()

class Caneta:
    def __init__(self, cor):
        # Guardamos a cor da caneta (ex: "blue", "red", "green", "bold yellow")
        self.cor = cor

    def escrever(self, texto):
        # O rich permite usar tags estilo BBCode com a variável da cor: [{self.cor}]
        console.print(f"[{self.cor}]{texto}[/{self.cor}]")


# Exemplo de uso:
caneta_azul = Caneta("cyan")
caneta_azul.escrever("Olá! Esta frase está sendo escrita com a caneta azul/ciano.")

caneta_vermelha = Caneta("bold red")
caneta_vermelha.escrever("Atenção! Esta frase está em vermelho e negrito.")
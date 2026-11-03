from abc import ABC, abstractmethod
import rich

class Cafeteira(ABC):
    def __init__(self, preparar, ferver = 0):
        self.preparar = preparar
        self.ferver = ferver
        
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass
    
    
    
class Cha(Cafeteira):
    def __int__(self, preparar, ferver, tipo_cha):
        super().__init__(preparar, ferver)
        self.tipo_cha = tipo_cha
        
    def misturar(self):
        rich.print(f"[bold green]Misturando o chá tipo:[/bold green] {self.tipo_cha}")
          
    def servir(self):
            rich.print(f"[bold yellow]Servindo o chá preparo {self.preparar} com fervura {self.ferver}[/bold yellow]")
        
class Cafe(Cafeteira):
    def __init__(self, preparar, ferver, tipo_cafe):
        super().__init__(preparar, ferver)
        self.tipo_cafe = tipo_cafe

    def misturar(self):
        rich.print(f"[bold green]Misturando o café tipo:[/bold green] {self.tipo_cafe}")

    def servir(self):
        rich.print(f"[bold yellow]Servindo o café preparo {self.preparar} com fervura {self.ferver}[/bold yellow]")


escolha_usuario = input("Escreva seu café: ")
escolha_usuario2 = input("Escreva seu cha: ")

meu_cafe = Cafe(preparar="Rápido", ferver=100, tipo_cafe=escolha_usuario)
meu_cha =  Cha(preparar="Rápido", ferver=100, tipo_cha=escolha_usuario2)
meu_cafe.misturar()
meu_cafe.servir()

meu_cha.misturar()
meu_cha.servir()
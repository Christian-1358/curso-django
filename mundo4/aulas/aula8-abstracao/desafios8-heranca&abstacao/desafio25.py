from abc import ABC, abstractmethod
import rich


class Transporte(ABC):
    def __init__(self, distancia: float):
        self.distancia = distancia
        self.frete = 0.0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete


class Caminhao(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete


class Drone(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete


distancia_usuario = float(input("Digite a distância da entrega (em km): "))


moto = Moto(distancia_usuario)
caminhao = Caminhao(distancia_usuario)
drone = Drone(distancia_usuario)


rich.print(f"[bold green]Frete de Moto:[/bold green] R$ {moto.calc_frete():.2f}")
rich.print(f"[bold yellow]Frete de Caminhão:[/bold yellow] R$ {caminhao.calc_frete():.2f}")
rich.print(f"[bold blue]Frete de Drone:[/bold blue] R$ {drone.calc_frete():.2f}")
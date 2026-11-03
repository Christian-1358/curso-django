from abc import ABC, abstractmethod
import math

# Classe abstrata Poligono
class Poligono(ABC):
    def __init__(self, qtd_lados: int):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

# Subclasse Quadrado
class Quadrado(Poligono):
    def __init__(self, lado: float):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2

# Subclasse Circulo
class Circulo(Poligono):
    def __init__(self, raio: float):
        super().__init__(qtd_lados=0)  # Círculo não possui lados retos
        self.raio = raio

    def perimetro(self):
        # Perímetro/Circunferência do círculo
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * (self.raio ** 2)
1. O que é Abstração?
Na programação, a abstração consiste em esconder a complexidade desnecessária e mostrar apenas os detalhes essenciais de um objeto ou conceito.

Pensa num carro: para o conduzir, precisas de saber usar o volante, os pedais e a mudança. Não precisas de saber exatamente como a centelha da vela de ignição acende o combustível no motor. O funcionamento interno complexo está "abstraído" de ti.

2. Classes Abstratas e Métodos Abstratos
Em Python (e noutras linguagens como Java ou C#), criamos a abstração através de classes abstratas.

Classe Abstrata: É um molde genérico que não pode ser instanciado diretamente (ou seja, não podes dar um objeto = NomeDaClasse()). Ela serve apenas como base/modelo para outras classes herdarem.

Método Abstrato: É um método que não tem corpo (usa-se pass ou fica vazio) na classe pai. Ele funciona como uma "regra" ou "contrato": obriga todas as subclasses que herdarem dessa classe a criarem a sua própria versão desse método.

3. Como se escreve em Python?
Para usar abstração em Python, usamos o módulo nativo abc (Abstract Base Classes):

Python
from abc import ABC, abstractmethod

# 1. Classe Abstrata (herda de ABC)
class Veiculo(ABC):
    def __init__(self, marca):
        self.marca = marca

    # Método abstrato (obrigatório para quem herdar)
    @abstractmethod
    def ligar_motor(self):
        pass

# 2. Subclasse concreta que cumpre o contrato
class Carro(Veiculo):
    def ligar_motor(self):
        return f"O motor do carro da {self.marca} roncou!"

        
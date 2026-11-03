
class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, valor):
        self.__base = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura = valor

    @property
    def medidas(self):
        return f"Base: {self.__base}, Altura: {self.__altura}"

    @property
    def area(self):
        return self.__base * self.__altura


# Testando a classe
r1 = Retangulo(10, 5)

print("Medidas:", r1.medidas)
print("Área:", r1.area)

# Alterando as medidas
r1.base = 20
r1.altura = 8

print("\nNovas medidas:", r1.medidas)
print("Nova área:", r1.area)

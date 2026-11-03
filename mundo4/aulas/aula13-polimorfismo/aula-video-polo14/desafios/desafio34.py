from abc import ABC, abstractmethod


class Funcionario(ABC):

  def __init__(self, nome: str, salario: float):
    self.nome = nome
    self.salario = salario

  @abstractmethod
  def calcular_bonus(self) -> float:
    pass


class Gerente(Funcionario):

  def calcular_bonus(self) -> float:
    return self.salario * 0.20  

class Designer(Funcionario):

  def calcular_bonus(self) -> float:
    return self.salario * 0.10  


class Desenvolvedor(Funcionario):

  def calcular_bonus(self) -> float:
    return self.salario * 0.15  


if __name__ == "__main__":
  gerente = Gerente("Ana", 8000.0)
  designer = Designer("Carlos", 4500.0)
  desenvolvedor = Desenvolvedor("Bruno", 6000.0)

  funcionarios = [gerente, designer, desenvolvedor]

  print("--- RELATÓRIO DE BÔNUS SALARIAL ---")
  for func in funcionarios:
    bonus = func.calcular_bonus()
    print(
        f"Funcionário: {func.nome} | Salário: R$ {func.salario:.2f} | "
        f"Bônus: R$ {bonus:.2f}"
    )
from abc import ABC, abstractmethod
import rich


class Funcionario(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.sal_bruto = 0.0
        self.salario = 0.0
        self.sal_min = 1612.0
        self.inss = 7.5 

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        if self.salario >= self.sal_min:
            rich.print(f"[bold green]{self.nome} ganha um salário igual ou superior ao mínimo ({self.salario:.2f}).[/bold green]")
        else:
            rich.print(f"[bold red]{self.nome} ganha abaixo do salário mínimo ({self.salario:.2f}).[/bold red]")


class Horista(Funcionario):
    def __init__(self, nome: str, valor_hora: float, horas_trab: float):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        desconto = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - desconto
        return self.salario


class Mensalista(Funcionario):
    def __init__(self, nome: str, sal_bruto: float):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        desconto = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - desconto
        return self.salario


horista = Horista("Carlos", valor_hora=50.0, horas_trab=160)
horista.calc_sal()
rich.print(f"[bold cyan]Salário Líquido (Horista - {horista.nome}):[/bold cyan] R$ {horista.salario:.2f}")
horista.analisar_sal()

print("-" * 40)

mensalista = Mensalista("Ana", sal_bruto=3500.0)
mensalista.calc_sal()
rich.print(f"[bold cyan]Salário Líquido (Mensalista - {mensalista.nome}):[/bold cyan] R$ {mensalista.salario:.2f}")
mensalista.analisar_sal()
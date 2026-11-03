
from abc import ABC, abstractmethod
from datetime import datetime
import rich

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: str):
        self._nome = nome
        self._nascimento = nascimento  

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def idade(self) -> int:
        """Calcula a idade dinâmica com base na data atual e data de nascimento."""
        try:
            # Tenta converter para formato dia/mês/ano ou ano-mês-dia
            if "/" in self._nascimento:
                data_nasc = datetime.strptime(self._nascimento, "%d/%m/%Y").date()
            else:
                data_nasc = datetime.strptime(self._nascimento, "%Y-%m-%d").date()
            
            hoje = datetime.now().date()
            # Diferença de anos ajustada pelo mês/dia do aniversário
            idade_calculada = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
            return idade_calculada
        except ValueError:
            return 0


class Aluno(Pessoa):
    cursos_oficiais = ["Python POO", "Algoritmos", "JavaScript", "Bancos de Dados"]

    def __init__(self, nome: str, nascimento: str, curso_inicial: str = None):
        super().__init__(nome, nascimento)
        self._curso = []
        if curso_inicial:
            self.add_curso(curso_inicial)

    @property
    def curso(self):
        """Retorna a lista de cursos inscritos pelo aluno."""
        return self._curso

    def add_curso(self, curso: str):
        """Adiciona um curso ao aluno caso seja válido/oficial."""
        if curso in self.cursos_oficiais:
            if curso not in self._curso:
                self._curso.append(curso)
                rich.print(f"[green]Curso '[bold]{curso}[/bold]' adicionado com sucesso para {self._nome}![/green]")
            else:
                rich.print(f"[yellow]O aluno {self._nome} já está matriculado em '{curso}'.[/yellow]")
        else:
            rich.print(f"[red]ERRO: O curso '{curso}' não é um curso oficial.[/red]")


if __name__ == "__main__":
    rich.print("[bold blue]=== TESTANDO O DESAFIO 033 ===[/bold blue]\n")

    aluno1 = Aluno(nome="Christian", nascimento="15/05/2008")

    rich.print(f"Aluno: [bold]{aluno1._nome}[/bold]")
    rich.print(f"Data de Nascimento: {aluno1.nascimento}")
    rich.print(f"Idade Atual: [bold green]{aluno1.idade} anos[/bold green]\n")

    aluno1.add_curso("Python POO")
    aluno1.add_curso("Algoritmos")
    
    aluno1.add_curso("Curso Não Existente")

    rich.print(f"\nCursos ativos do aluno: {aluno1.curso}")
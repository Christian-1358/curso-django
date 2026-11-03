from pessoas import Pessoa


class Aluno(Pessoa ): #colocando o (Pessoa/nome da classe) ele fica dentro da herança
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curos = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer a matricula")
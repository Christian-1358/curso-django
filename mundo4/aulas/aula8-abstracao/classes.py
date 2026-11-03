from abc import ABC, abstractclassmethod # Abstract Base Classes 


class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
        
    def fazer_ainiversario(self):
        self.idade += 1 

    @abstractclassmethod
    def estudar(self):
        pass

class Aluno(Pessoa ): #colocando o (Pessoa/nome da classe) ele fica dentro da herança
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curos = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer a matricula")

    def estudar(self):
        print(f"{self.nome} esta estudando {self.curos} na turma {self.turma} ")
    
class Funcionario(Pessoa):
    def __int__(self, nome, cargo, setor, idade):
        super().__init__(self, nome, idade)
        self.cargo = cargo
        self.setor = setor
        
    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")
    
    def estudar(self):
            print(f"{self.nome } é especialista em {self.especialidade} no {self.nivel} ")
            
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
        
    def dar_aula(self):
        print(f"{self.nome} começou a dar aula")
    
    def estudar(self):
        print(f"{self.nome} se especializa para area de {self.cetor}")
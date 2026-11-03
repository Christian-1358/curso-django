from pessoas import Pessoa


    
class Funcionario(Pessoa):
    def __int__(self, nome, cargo, setor, idade):
        super().__init__(self, nome, idade)
        self.cargo = cargo
        self.setor = setor
        
    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")
    
    
    
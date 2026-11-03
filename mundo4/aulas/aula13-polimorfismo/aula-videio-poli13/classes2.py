class Mae:
    def __init__(self, nome:str = "mamae"): #ATributos
        self.nome = nome
        
    def fazer_pudim(self): #objetos
        print(f"{self.nome} faz pudin com leite condeçado")
    
    
    def fritar_coxinha(self):
        print(f"{self.nome} faz coxinha com olho de soja")


class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com creme de morcego!")


class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} faz coxinha com os dentes")
class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
        
    def fazer_ainiversario(self):
        self.idade += 1 
import rich

class Funcionarios:
    def __init__(self, nome, setor, cargo):
        self.nome = nome 
        self.setor = setor
        self.cargo = cargo
        
    def __str__(self):
        return f"Olá, meu nome é {self.nome}, meu setor é {self.setor}, e meu cargo atualmente é {self.cargo}"
        
        


c1 = Funcionarios('Christian', 'DEV', 'Trabaiador')
rich.inspect(c1)

c2 = Funcionarios('Paula', 'TI', 'mosca')
print(c2)
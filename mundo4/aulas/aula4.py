class Gafanhoto:
    def __init__(self): #metodo contrutor
        #atributos de instancia
        self.nome = ""
        self.idade = 0
        
    def aniversario(self):
        self.idade = self.idade + 1
        
        
    def mensagem(self):
        return f'{self.nome}, é gafanhoto(a)  e tem {self.idade}, anos de idadeee'


#declarações de objeto
g1 = Gafanhoto()
g1.nome == 'maria'
g1.idade == 17
g1.aniversario()

print(g1.mensagem())





'''class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    def barulho(self):
        return "som generico"

class Cachorro(Animal):
    def barulho(self):
        return "Au Au"

'''
    

            
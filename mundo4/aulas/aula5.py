#melhorando codigo aula4

class Gafanhoto:
    # Quando eu coloco """ eu crio uma Documentação, q com isso se eu colocar: print(g1.__doc__) ele ira mostrar a documentação da minha classe
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    
    Para criar uma nova pessoa, use:
    
    Variavel = Gafanhoto(nome, idade)
    
    """
    def __init__(self, nome = "vazio", idade = 0): #metodo contrutor
        #atributos de instancia
        self.nome = nome
        self.idade = idade
        
        
    def aniversario(self):
        self.idade = self.idade + 1
        
    
    def __str__(self): # Dunder Method 
        return f"{self.nome}, é gafanhoto(a)  e tem {self.idade}, anos de idadeee"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
#declarações de objeto
g1 = Gafanhoto("Maria", 15)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__) # para ver o nome da classe para poder ver o objeto 

g2 = Gafanhoto("Mauro", 52)
print(g2)
print(g2.__getstate__())


"""

print(g1.__getstate__) #Attrubute # faz mesma coisa q o __dict__ # mas no __getstate__ , vc pode usar um def
print(g1.__dict__())#Method # vai mostrar a dicionario usando o __dict__

print(g1.__doc__)"""
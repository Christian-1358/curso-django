# POLIMORFISMO (ese codigo é de inclusao)



from abc import ABC, abstractclassmethod


class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome
       
    @abstractclassmethod   
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e esta emitindo um som")    
        
        
class Pato(Animal):
        def emitir_som(self):
            print(f"{self.nome} faz quack quack") 



class Gato(Animal): 
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer miau miau")


class Galinha(Animal):
        def emitir_som(self):
            print(f"{self.nome} faz pi pi pi")


# cachorro :

class Chachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} faz auau")
        
class Spitz(Chachorro):
    def emitir_som(self):
        print(f'{self.nome} latiu auauauauauauuaauauuauauuauauaauau')

class Pitubul(Chachorro):
    def emitir_som(self):
        print(f"{self.nome} disse rulf rulf")



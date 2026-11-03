

class Avaliacoes:
    
    def __init__(self, nome, diciplina, nota = 0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota #atributo protegido
        
        
        # Criando produto validavel 
        
        @property
        def nota(self): #getter
            return self._nota
        
        @nota.setter
        def  nota(self, valor): #setter 
            if 0 <= valor <= 10:
                self._nota = valor
            else:
                print("nota invalida")
        
        
        
        
        

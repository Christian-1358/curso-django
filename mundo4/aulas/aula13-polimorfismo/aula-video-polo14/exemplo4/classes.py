class Numero:
    
    def __init__(self, valor: int | float = 0):
        self.valor = valor
    
    def dobrar(self):
        self.valor = self.valor * 2
    
    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do numero"
    
class Texto:
    def __init__(self, txt: str = ''):
        self.texto = txt
    
    def dobrar(self):
        self.textp = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do Texto"    

class Lista:
        
    def __init__(self, lst:list = []):
        self.valores = lst
    
    def dobrar(self):
        self.valores = self.valores + self.valores 
       
    def __str__(self):
        return f"Tenho os itens {self.valores} dentro da Lista"
     
class Papel:
        
    def __init__(self,):
        self.dobrado = False
    
    def dobrar(self):
        self.dobrado = True
    
    def __str__(self):
            return f"O papel esta {'novo' if not self.dobrado else 'dobrado' }"
class Casa:
        
    def __init__(self):
        pass
    
    def __str__(self):
        return f"Era uma casa muito engraçada.."
    
    
# DUck typing


def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldades para dobrar {objeto.__class__.__name__}")
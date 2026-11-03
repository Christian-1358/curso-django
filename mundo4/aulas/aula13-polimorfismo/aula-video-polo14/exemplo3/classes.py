class Porta:  
    def abrir(self):
        print(f"girar a maçaneta e empurrar/puxar a porta") 
    
    
class Empresa:
    def abri(self):
        print(f"Va ai portal do empredendor e com todoa documentação para abrir o cnpj")
    
    
class Ovo:
    def abrir(self):
        print(f"Quebre o ovo")
        


class Pedra:
    pass


# METODO PYTHONICO POLIMORFICO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        (f"encontrei problemas ao tentar abrir um objeto tipo {objeto.__class__.__name__}")
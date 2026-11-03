from functools import singledispatchmethod



class Analizador():
    
    @singledispatchmethod
    def analizar(self, valor):
        print(f"Nao foi possivel analizar o valor {valor}")
        
    @analizar.register
    def _(self, valor: int):
        print(f"{valor} é um numero inteiro")
        
    @analizar.register
    def _(self, valor: str):
        print(f"{valor} é uma cadeia de caracteres")
    
    @analizar.register
    def _(self, valor: tuple|list|dict):
        print(f"{valor} é  uma coleção de dados")
        
    @analizar.register
    def _(self, valor: float):
        print(f"seu valor é {valor}")
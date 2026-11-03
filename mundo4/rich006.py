from rich import print
from rich import inspect

class ContaBancaria:
    """
Crie uma conta bancaria e permita fazer saque e depositos
    """
    
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criado com sucesso, saldo atual de {self.saldo:,.2f}")
        
    def __str__(self):
        return f"A conta {self.id} de {self.titular}, possue valor de R${self.saldo:,.2f}"
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de falor R${valor:,.2f} autorizado na conta de {self.id}")
        
    def sacar(self, valor):
            if valor > self.saldo:
                print( f"Você Não pode sacar essse valor")
            else:
            
            
                self.saldo -= valor    
            
            print(f"Saque de falor R${valor:,.2f} autorizado na conta de {self.id}")


        
        
        
c1 =  ContaBancaria(122, "chris", 3000)
inspect(c1)
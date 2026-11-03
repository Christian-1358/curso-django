class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id #publico (+)
    
        self._titular = nome
        self.__saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}")

    @property
    def saldo(self):
        """Retorna o saldo da conta sem expor o atributo interno."""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.__saldo = valor

    def __str__(self):
      #  return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo."
        return f"estado atual da conta {self.__dict__}"
    
    
    def depositar(self, valor):
        valor =  abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta {self.id} ")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque NEGADO de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado na conta {self.id} ")
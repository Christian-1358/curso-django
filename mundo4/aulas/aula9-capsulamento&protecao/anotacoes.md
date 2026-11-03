Tema: Encapsulamento em Python (Público, Protegido e Privado - Parte 1) 
  Visibilidade de Atributos e Métodos:Público: Acessível de qualquer lugar (dentro e fora da classe).  
   Protegido: Indicado por um sublinhado simples (_), sugerindo acesso apenas dentro da classe e de suas subclasses.   
   Privado: Indicado por duplo sublinhado (__), restrito estritamente ao escopo da própria classe onde foi definido.   

   exemplo codigo;  

   class ContaBancaria:
    def __init__(self, titular, saldo, senha):
        self.titular = titular          # Público (acessível de qualquer lugar)
        self._agencia = "001-X"         # Protegido (convenção: uso interno ou em subclasses)
        self.__senha = senha            # Privado (restringe o acesso direto fora da classe)

    # Método público para ver o saldo (boa prática para aceder a privados)
    def mostrar_saldo(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.__consultar_saldo_interno()}"

    # Método privado (só pode ser chamado dentro desta classe)
    def __consultar_saldo_interno(self):
        return 1500.00


# --- Testando o código ---
conta = ContaBancaria("Carlos", 1500.00, "1234")

# 1. Atributo Público: Acesso direto permitido
print(conta.titular)  # Saída: Carlos

# 2. Atributo Protegido: Acesso permitido, mas desencorajado fora da classe/subclasses
print(conta._agencia)  # Saída: 001-X

# 3. Atributo Privado: Dá erro se tentares aceder diretamente (gera AttributeError)
# print(conta.__senha) 

# Aceder através de um método público da classe
print(conta.mostrar_saldo())  # Saída: Titular: Carlos | Saldo: R$ 1500.0
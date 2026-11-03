import rich


class ContaBancaria:
    def __init__(self, id_conta: int, titular: str, senha: str, saldo_inicial: float = 0.0):
        self._id = id_conta
        self._titular = titular
        
        self.__saldo = saldo_inicial
        self.__hash = hash(senha)  

    @property
    def nome(self):
        """Propriedade pública (+) para aceder ao nome do titular."""
        return self._titular

    def _validar_senha(self, chave: str) -> bool:
        """Método interno para validar a senha/chave informada."""
        return hash(chave) == self.__hash

    def _pede_senha(self) -> str:
        """Pede a senha ao utilizador no terminal."""
        return input("Digite a sua senha: ")

    def depositar(self, valor: float):
        """Método para realizar depósitos na conta."""
        if valor > 0:
            self.__saldo += valor
            rich.print(f"[green]Depósito de R$ {valor:.2f} realizado com sucesso![/green]")
        else:
            rich.print("[red]ERRO: O valor do depósito deve ser maior que zero.[/red]")

    def sacar(self, valor: float, chave: str = None):
        """Método para realizar levantamentos/saques mediante validação de senha."""
        if chave is None:
            chave = self._pede_senha()

        if not self._validar_senha(chave):
            rich.print("[red]ERRO: Senha incorreta! Operação cancelada.[/red]")
            return

        if valor <= 0:
            rich.print("[red]ERRO: Valor de saque inválido.[/red]")
            return

        if valor > self.__saldo:
            rich.print(f"[red]ERRO: Saldo insuficiente. Saldo atual: R$ {self.__saldo:.2f}[/red]")
            return

        self.__saldo -= valor
        rich.print(f"[green]Saque de R$ {valor:.2f} efetuado com sucesso![/green]")
        rich.print(f"[yellow]Saldo restante: R$ {self.__saldo:.2f}[/yellow]")


if __name__ == "__main__":
    conta = ContaBancaria(id_conta=101, titular="Christian", senha="1234", saldo_inicial=500.0)

    rich.print(f"Conta criada para o titular: [bold blue]{conta.nome}[/bold blue]\n")

    conta.depositar(200.0)

    rich.print("\n--- Tentativa de Saque ---")
    conta.sacar(valor=150.0, chave="1234")

    rich.print("\n--- Tentativa com Senha Incorreta ---")
    conta.sacar(valor=50.0, chave="0000")
from abc import ABC, abstractmethod


class Mensagem(ABC):

  def __init__(self, mensagem: str, tipo: str, icone: str):
    self._mensagem = mensagem  
    self._tipo = tipo  
    self._icone = icone  

  @abstractmethod
  def mostrar(self) -> str:
    """Método abstrato mostrar()"""
    pass


class Erro(Mensagem):

  def __init__(self, mensagem: str):
    super().__init__(mensagem, "Erro", "❌")

  def mostrar(self) -> str:
    return f"{self._icone} [{self._tipo}]: {self._mensagem}"


class Aviso(Mensagem):

  def __init__(self, mensagem: str):
    super().__init__(mensagem, "Aviso", "⚠️")

  def mostrar(self) -> str:
    return f"{self._icone} [{self._tipo}]: {self._mensagem}"


if __name__ == "__main__":
  # Instanciação das diferentes mensagens padronizadas
  msg_erro = Erro("Falha crítica ao ligar à base de dados.")
  msg_aviso = Aviso("O espaço em disco está quase esgotado.")

  sistema_mensagens = [msg_erro, msg_aviso]

  print("--- SISTEMA DE MENSAGENS PADRONIZADAS ---")
  for msg in sistema_mensagens:
    print(msg.mostrar())
    print("-" * 50)
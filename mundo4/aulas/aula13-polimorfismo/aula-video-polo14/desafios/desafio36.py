from abc import ABC, abstractmethod


class Pagamento(ABC):

  def __init__(self, valor: float):
    self._valor = valor 
  @property
  def fvalor(self) -> str:
    """Propriedade formatada (@fvalor)"""
    return f"R$ {self._valor:.2f}"

  @property
  def valor(self) -> float:
    return self._valor

  @abstractmethod
  def pagar(self) -> str:
    """Método abstrato pagar()"""
    pass


class Boleto(Pagamento):

  def __init__(self, valor: float, codigo_barras: str):
    super().__init__(valor)
    self.codigo_barras = codigo_barras

  def pagar(self) -> str:
    return (
        f"A processar o pagamento de {self.fvalor} através de Boleto Bancário."
        f" Código de barras: {self.codigo_barras}"
    )


class PIX(Pagamento):

  def __init__(self, valor: float, chave: str):
    super().__init__(valor)
    self.chave = chave

  def pagar(self) -> str:
    return (
        f"A processar o pagamento instantâneo de {self.fvalor} via PIX (Chave:"
        f" {self.chave})."
    )


class Credito(Pagamento):

  def __init__(self, valor: float, parcelas: int):
    super().__init__(valor)
    self.parcelas = parcelas

  def pagar(self) -> str:
    return (
        f"A processar o pagamento de {self.fvalor} com Cartão de Crédito em"
        f" {self.parcelas}x."
    )


if __name__ == "__main__":
  # Instanciação dos diferentes tipos de pagamento
  pagamento_boleto = Boleto(150.75, "34191.79001 01043.510018...")
  pagamento_pix = PIX(89.90, "usuario@email.com")
  pagamento_credito = Credito(1250.00, 10)

  transacoes = [pagamento_boleto, pagamento_pix, pagamento_credito]

  print("--- SIMULADOR DE GESTÃO DE PAGAMENTOS ---")
  for transacao in transacoes:
    print(transacao.pagar())
    print("-" * 65)
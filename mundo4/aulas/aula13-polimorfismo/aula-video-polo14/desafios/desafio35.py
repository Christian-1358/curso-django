from abc import ABC, abstractmethod


class Arquivo(ABC):

  def __init__(self, nome: str, extensao: str, tamanho: float):
    self.nome = nome
    self._extensao = extensao
    self.tamanho = tamanho

  @property
  def nome_completo(self) -> str:
    return f"{self.nome}.{self._extensao}"

  @abstractmethod
  def abrir(self) -> str:
    pass


class PDF(Arquivo):

  def __init__(self, nome: str, tamanho: float, num_paginas: int):
    super().__init__(nome, "pdf", tamanho)
    self.num_paginas = num_paginas

  def abrir(self) -> str:
    return (
        f"A abrir o documento PDF '{self.nome_completo}' com"
        f" {self.num_paginas} páginas..."
    )


class DOC(Arquivo):

  def __init__(self, nome: str, tamanho: float, autor: str):
    super().__init__(nome, "doc", tamanho)
    self.autor = autor

  def abrir(self) -> str:
    return (
        f"A abrir o documento DOC '{self.nome_completo}' criado por"
        f" {self.autor}..."
    )


if __name__ == "__main__":
  # Instanciar diferentes tipos de ficheiro
  f1 = PDF("relatorio_financeiro", 4.2, 25)
  f2 = DOC("carta_apresentacao", 1.1, "João Silva")

  lista_ficheiros = [f1, f2]

  print("--- SIMULADOR DE ABERTURA DE FICHEIROS ---")
  for ficheiro in lista_ficheiros:
    print(f"Nome completo: {ficheiro.nome_completo}")
    print(f"Tamanho: {ficheiro.tamanho} MB")
    print(ficheiro.abrir())
    print("-" * 45)
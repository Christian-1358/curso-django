from abc import ABC, abstractmethod
import re


class Validador(ABC):

  @abstractmethod
  def validar(self) -> bool:
    """Método abstrato validar()"""
    pass


class Usuario(Validador):

  def __init__(self, nome: str):
    self.nome = nome

  def validar(self) -> bool:
    return len(self.nome.strip()) >= 3


class Email(Validador):

  def __init__(self, endereco_email: str):
    self.endereco_email = endereco_email

  def validar(self) -> bool:
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, self.endereco_email))


class Senha(Validador):

  def __init__(self, palavra_passe: str):
    self.palavra_passe = palavra_passe

  def validar(self) -> bool:
    return len(self.palavra_passe) >= 6


if __name__ == "__main__":
  validador_usuario = Usuario("Carlos")
  validador_email = Email("suporte@exemplo.com")
  validador_senha = Senha("segredo123")

  validadores = [validador_usuario, validador_email, validador_senha]

  print("--- SISTEMA DE VALIDAÇÃO DE DADOS ---")
  for v in validadores:
    tipo = v.__class__.__name__
    resultado = v.validar()
    status = "Válido ✅" if resultado else "Inválido ❌"
    print(f"Validador [{tipo}]: {status}")
    
    
    
    

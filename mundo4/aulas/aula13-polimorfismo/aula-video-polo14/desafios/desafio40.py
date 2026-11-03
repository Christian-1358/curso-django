import json
import xml.etree.ElementTree as ET


class Aluno:

  def __init__(self, nome: str, curso: str, serie: str):
    self.nome = nome  
    self.curso = curso  
    self.serie = serie  


class Usuario:

  def __init__(self, nome: str, email: str):
    self.nome = nome  
    self.email = email 


class JSON:

  @staticmethod
  def exportar(obj) -> str:
    return json.dumps(obj.__dict__, ensure_ascii=False, indent=4)


class XML:

  @staticmethod
  def exportar(obj) -> str:
    root_name = obj.__class__.__name__.lower()
    root = ET.Element(root_name)
    for chave, valor in obj.__dict__.items():
      child = ET.SubElement(root, chave)
      child.text = str(valor)
    return ET.tostring(root, encoding="utf-8").decode("utf-8")


if __name__ == "__main__":
  aluno = Aluno("Beatriz Costa", "Programação Avançada", "9º Ano")
  usuario = Usuario("Marcos Lima", "marcos.lima@exemplo.com")

  print("=== EXPORTAÇÃO PARA JSON ===")
  print("--- Aluno ---")
  print(JSON.exportar(aluno))
  print("--- Usuário ---")
  print(JSON.exportar(usuario))

  print("\n=== EXPORTAÇÃO PARA XML ===")
  print("--- Aluno ---")
  print(XML.exportar(aluno))
  print("--- Usuário ---")
  print(XML.exportar(usuario))
class Produto:
    
  def __init__(self, nome: str, preco: float):
    self.nome = nome 
    self.preco = preco 


class Carrinho:

  def __init__(self):
    self.produtos = []

  @property
  def total(self) -> float:
    """Propriedade @total que calcula a soma dos preços dos produtos[cite: 5]"""
    return sum(p.preco for p in self.produtos)

  def __add__(self, produto: Produto):
    if isinstance(produto, Produto):
      self.produtos.append(produto)
    return self


if __name__ == "__main__":
  p1 = Produto("Teclado Mecânico", 350.00)
  p2 = Produto("Rato Gamer", 150.50)
  p3 = Produto("Monitor Ultrawide", 1800.00)

  carrinho = Carrinho()

  carrinho + p1 + p2 + p3

  print("--- CARRINHO DE COMPRAS (AGREGAÇÃO) ---")
  for prod in carrinho.produtos:
    print(f"Produto: {prod.nome} | Preço: R$ {prod.preco:.2f}")

  print("-" * 45)
  print(f"Valor Total do Carrinho: R$ {carrinho.total:.2f}")
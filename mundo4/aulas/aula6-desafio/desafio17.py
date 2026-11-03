class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}"


p1 = Produto("Mouse", 59.90)
print(p1.etiqueta())
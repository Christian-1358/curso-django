class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.pagina_atual = 0

    # Aqui está o nosso método para exibir a ficha do livro:
    def mostrar_ficha(self):
        print("--- FICHA DO LIVRO ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Página atual: {self.pagina_atual}")
        print("----------------------")

# Testando a criação e chamando o método:
meu_livro = Livro("Doutor Nerfario", "Chris", 2000)
meu_livro.mostrar_ficha()
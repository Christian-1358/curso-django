
class Diario:
    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)
        print("Segredo guardado com sucesso!")

    def ler(self, senha):
        if senha == self.__senha:
            print("\n--- MEU DIÁRIO ---")

            if len(self.__segredos) == 0:
                print("O diário está vazio.")
            else:
                for segredo in self.__segredos:
                    print(segredo)
        else:
            print("Senha incorreta! Acesso negado.")


# Criando o diário
meu_diario = Diario("1234")

while True:
    print("\n=== DIÁRIO SECRETO ===")
    print("1 - Escrever no diário")
    print("2 - Ler o diário")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mensagem = input("Digite seu segredo: ")
        meu_diario.escrever(mensagem)

    elif opcao == "2":
        senha = input("Digite a senha: ")
        meu_diario.ler(senha)

    elif opcao == "3":
        print("Saindo do diário...")
        break

    else:
        print("Opção inválida!")

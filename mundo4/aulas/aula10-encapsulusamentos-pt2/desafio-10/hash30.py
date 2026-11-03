from desafio30 import Credencial


def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: "))
    print(c.senha)
    c.validar('teste')

'''    c.validar('CeV!@')''' 

if __name__ == '__main__':
    main()
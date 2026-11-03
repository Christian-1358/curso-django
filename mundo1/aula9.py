#25| Crue um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input(str("Digite seu nome completo: ")).strip()

if nome.upper().find("SILVA") >= 0:
    print("O nome contém 'SILVA'.")
else:
    print("Não contem 'SILVA' no nome. ")


"""

#24| CRIE UM programa que leia o nome de uma cidade e diga se elacomeça ou nao com o nome "santo" .

cidade = input(str  ("Digite o nome da cidade: ")).strip()

#add o comando de if ali, só pra descaso, nem prefisava, era só pra deixar o comando mais completo (base: cidade[:5].upper() == "SANTO":)
if cidade[:5].upper() == "SANTO":
    print("A cidade começa com o nome de 'SANTO'.")
else:
    print("ERRO! Não existe cidade que começa com nome de 'SANTO'.")

"""

#23| faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
'''
numero = int(input("Digite um número de 0 a 9999: "))

print("Unudade: {}".format(numero // 1  % 10))
print("Dezena {}".format(numero // 10 % 10))
print("centena {}".format(numero // 100 % 10))
print("milhar {}".format(numero // 1000 % 10))


'''
#22| programa que leia o nome completo de uma pessoa e mostre : quantas letras ao todo (Sem espaço), quantas letras do primeiro nome 
'''

nome = input(str("Digite seu nome completo: "))


print("Nomes com letras maiusculas: ", nome.upper())
print("NOmes com letras minusculas: ", nome.lower())
print("Quantidade de letras ao todo (sem espaço):", len(nome) - nome.count(" "))
print("Quantidade de letras no primeiro nome: ", len(nome.split()[0]))

'''
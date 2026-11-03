'''#80
lista = []

for c in range(5):
    numero = int(input("Digite um número: "))
    lista.append(lista)
    lista.sort()
    print(lista)
    print(f"Todos valores cadastrados dentro da lista: {lista}")
    

'''





'''#79
lista = []



while True:
    numero = int(input("Digite um número: "))

    if numero in lista:
        print("Esse número já está na lista!")
    else:
        lista.append(numero)

    continuar = input("Quer continuar? [S/N]: ")

    if continuar in "Nn":
        break

lista.sort()

print(lista)'''
    
  





'''#78
lista = []
contador = 0

while contador < 5:
    
    numero = int(input("Digite 5 numeros para ser armazenados dentro da lista: "))
    lista.append(numero)
    contador += 1
    maior = lista[0]
    menor = lista[0]
for n in lista:

    if n < menor:
        print(f"Menor numero da lista: {menor}")
    elif n > maior:
        print(f"Maior numero da lista: {maior}")
    print(f'dados lista: {n}')
    
for posicao, n in enumerate(lista):
    print(f"Número: {n} | Posição: {posicao}")



'''










'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
#para poder deixar sem as : []
for v in valores:
    print(f'{v}...', end='')
'''




'''letra = str(input("Digite [S/N] se sim, vc ira add um item, senao vc ira sair, ou digite remover para remover todos os itens:  ").upper())

lista = [ ]

if letra == 'S' or letra == 's':
    nome = str(input("Digite o nome do que vc quer add: "))
    lista.append(nome)
    print(lista)
elif lista == 'remover' or lista == "REMOVER":
    lista.remove()

else:
    print("saindo")
    exit()
    '''
   



#len| conta os elementedos = len(lista)


'''num = [2,5,9,1]
num [3] = 3
num.append(7)
num.sort(2, 2)
num.remove(2)
print(num)
print(f"Essa lista tem {len(num)} elementos")'''

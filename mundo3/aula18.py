
#87| tem que voltar pra outro la
#86| tem que voltar pra outro la


'''#85
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor) 
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print("-=" * 30)
print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores ímpares digitados foram: {num[1]}")




'''











''''#84
temp = list()
principal = list()
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
            
    principal.append(temp[:])
    temp.clear()
    
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'B) O maior peso foi de {maior}kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()

print(f'C) O menor peso foi de {menor}kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()


'''











'''galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 5):
    dados.append(str(input("nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:]) # [:] cria uma copia de dados
    dados.clear()
    
    print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade:")
        totmai += 1

    else:
        print("f{p[0]} é menor de idade")
        totmen += 1
        
        
    print(f"Temos {totmai} maiores e {totmen} menosres de idade")
'''




'''galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]

for p in galera:
    print(f'p[0] tem {p[1]} anos de idade.')

'''





'''    teste = list()
    teste.append('gustavo')
    teste.append(40)

    galera = list()
    galera.append(teste[:])
    teste[0] = 'maria'
    teste[1] = 22
    print(teste[galera])'''
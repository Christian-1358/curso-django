#55
peso = []
for p in range(5):
    pesso_pessoa = float(input("Digite o pesso da pesoa KG: "))
    peso.append(pesso_pessoa)
print(f"Maior peso: {max(peso)} kg")
print(f"Menos peso: {min(peso)} kg")




#54 (49 n dava pra fazer) 
"""
ano_atual = 2026

maiores = []
menores = []


for pessoas in range(0, 7):
    pessoa = str(input("Digite o nome da pessoa:"))
    anos = int(input("Digite o ano de nascimento: "))
    if ano_atual - anos >= 18:
        maiores.append(pessoa)
    else: 
        menores.append(pessoa)

print("Mairores de idade: ", maiores)
print("Menores de idade:", menores )

"""
#48 | fiz, mas pedi ajuda um pouco pro chat
"""
soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c 
        print(soma)

"""
"""
#47| 
for numero in range(2, 51, 2):
    print(numero)

"""


"""
#46| Faça um programa q mostre na tela uma contagem regreciva para o estouro de fogos de artificio, inde de 10 até 0, com uma pausa de um segundo antre eles
import time

for c in range(10, 0, -1):
    print(c),time.sleep(1)
print("ESTOROU")
"""
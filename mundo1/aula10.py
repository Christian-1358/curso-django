#33| faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
else:
    maior = numero3
    print(f"O maior número é: {maior}")
    """


#32| Faça um programa que lia o ano qualquer e mostre se  ela é bissexto
"""
ano = int(input("Digite um ano qualquer: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
"""
#31| Desenvolta um proigrama que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

pergunta = float(input("Digite a distância da viagem em Km: "))
if pergunta <= 200:
    preco = pergunta * 0.50
else:
    preco = pergunta * 0.45
print("O preço da passagem é de R${:.2f}".format(preco))
"""


#30| Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
"""
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é ímpar.")
    

"""

#29|escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidae = float(input("Digite a velocidade do carro (em Km/h): "))
if velocidae > 80:
    multa = (velocidae - 80) * 7
    print("Você foi multado! O valor da multa é de R${:.2f}".format(multa))
else:
    print("Você está dentro do limite de velocidade.")

"""
#28| escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
numero_computado = randint(0, 5)
numero_user = int(input("Tente adivinhar o número que o computador pensou (entre 0 e 5): "))
if numero_user == numero_computado:
    print("Parabéns! Você acertou.")
else:
    print("Que pena! Você errou.")
    """
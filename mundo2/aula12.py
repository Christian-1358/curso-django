#44| 
produto_lista = {
    "rapadura": 1.00,
    "coca":  6.00,
    "arroz": 10.00,
    "massa": 14.00,
    "peixe": 13.00,
}
print("Produtos disponiveis")
for produto in produto_lista:
    print(produto)
escolha = str(input("Digite o nome do produto que vc quer:"))
if escolha in produto_lista:
    print(f"Preço: R${produto_lista[escolha]:.2f}")
else:
    print("Produto não encontrado.")

#41| A confederação Nacional de nataçao precisa de um programa que leia o ano de nasimento de um atleta e mostre sua categoria , de acordo com a idade 
"""
idade = int(input("Digite sua idade:"))

if idade <= 9:
    print("Vocẽ é mirin")
elif idade <= 14:
    print("Voce é infantil")
elif idade <= 19:
    print("Voce é junior")
elif idade <= 20:
    print("Senior")
else:
    print("Master")
"""



#40| Crie um programa que leia 2 notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atiginda
# - Media abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9: RECUPERACAO
# - Media 7.0 ou superior: APROVADO 
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))

soma_nota = ( nota1 + nota2 ) /2

if soma_nota <= 5.0:
    print("Sua nota {}, é abaixo da média da escola, você esta REPROVADO".format(soma_nota))
elif 5.0 <= soma_nota <= 6.9:
    print("Sua nota {}, Você está de RECUPERAÇÂO".format(soma_nota))
else:
    soma_nota > 7.0 
    print("PARABENS, sua nota é {}, você esta aprovado!!!".format(soma_nota))
"""

#39| Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade : 
# -Se ele ainda vai se alistar ao seriço militar
# -Se é a hora de se alistar
# -Se já passou do tempo de alistamento
#Seu programa tambem devara mostrar o tempo que falta ou que passou do prazo
"""
ano_nasmento = int(input('Digite o ano de nascimento do jovem: '))
ano_atual = 2026

idade = ano_atual - ano_nasmento

if idade < 18:
    anos_faltando = 18 - idade
    print("Você tem {}, falta ainda para você se alistar".format(anos_faltando))
elif idade == 18:
    print("Você tem {}, você tem que se alistar!".format(idade))
else:
    idade > 19
    print("Você tem {}, ja passou seu tempo de alistamento!".format(idade))

"""


#38 | escreva um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem: 
# -O primeiro valor é maior -O segundo valor é maior 
# -O segundo valor é maior 
# -Não existe valor maior, os dois são iguais
"""
numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo numero inteiro: '))

if numero1 > numero2:
    print ('O primeiro valor é maior.')
elif numero2 > numero1:
    print ('O segundo valor é maior.')
else:
    print("Não existe valor maior os 2 sao iguais!")
    
"""


#36| programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, 
# o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, 
# sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado.
"""
emprestimo = float(input('Qual o valor do emprestimo? '))
salario = float(input('Qual o salario do comprador? '))
anos = int(input('Em quantos anos ele vai pagar? '))

if anos <= 0:
    print('O número de anos deve ser maior que zero.')
else:
    prestacao_mensal = emprestimo / (anos * 12)
    limite = salario * 0.3

    print(f'Valor da prestação mensal: R${prestacao_mensal:.2f}')
    print(f'Limite de 30% do salário: R${limite:.2f}')

    if prestacao_mensal > limite:
        print('Empréstimo negado! A prestação excede 30% do salário.')
    else:
        print('Empréstimo aprovado! A prestação está dentro do limite.')
        
        """
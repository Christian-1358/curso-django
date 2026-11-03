
homens = 0
mulheres = 0
menores = 0
mulheres_menos_20 = 0

while True:

    idade = int(input("Digite sua idade: "))

    sexo = input("Digite seu sexo [M/F]: ").upper()

    if idade < 18:
        menores += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        mulheres += 1

        if idade < 20:
            mulheres_menos_20 += 1

    print("=-" * 20)

    continuar = input("Deseja continuar? [N/S]: ")

    if continuar == 'N':
        break

print(f"Menores de 18 anos: {menores}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres cadastradas: {mulheres}")
print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")



"""#66
n = s = 0
while True:
    n = int(input("Digite um numero"))
    if n == 999:
        break
    s += n
    print(f'soma {s}')
print("terminou")
"""
"""
#68:
import random
vitorias = 0
while True:
    escolha = input("vc escolhe par ou impar [p/i]:")
    
    if escolha not in ("p", 'i'):
        print("Escreva novamente")
        continue
    jogardor = int("Digite seu numeroo: ")
    computador = random.randint(0, 10)
    soma =  jogardor + computador
    
    resultado = 'p' if soma % 2 == 0 else 'i'
    
    print(f"O computador escolheu {computador}. soma: {soma} ")
    
    if resultado == escolha:
        vitorias += 1
        print("Voce venceu")
    else: print("vc perdeu")
    break 

print('vitorias consecutivas {}'.format(vitorias))
    

"""





'''
n = s = 0
while True:
    n = int(input("DIgite um numero: \n"))
    if n == 999:
        break    
    s += n  
print(" A soma vale {}".format(s))
   '''
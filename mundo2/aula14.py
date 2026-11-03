




#58
'''
s = 0
while s == 0:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    c = input("Digite [1] para somar\n"
           "Digite [2] para multiplicar\n"
           "Digite [3] para maior\n"
           "Digite [4] novos números\n"
           "Digite [5] para sair\n"
          )
    if c == "1":
        soma = n1 + n2
        print("A soma dos dois numeros são: {}".format(soma))
        print(c)
    elif c == '2':
        multiplicador = n1 * n2
        print("A multiplicação dos dois numeros são: {}".format(multiplicador))
        print(c)
    elif c == '3':
        if n1 > n2:
            print("O primeiro numero é maior")
        elif n2 > n1:
            print("O segundo numero é maior")
        else:
            print("Os dois numeros sao iguais")
            print(c)
    elif c == '4':
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
        print(c)
    elif c == '5':
        print("saindo ...")
        exit()
        


'''
#57
'''
s = 1
while s == "M" or "F":
    n = str(input("Digite o sexto do bb [M/F]")).upper()
    if n == "M":
        print("Parabens o bebe é masculino")
        exit()
    elif n == "F":
        print("Parabens o bebe é feminino")
        exit() 
    else: 
        print("ERRO, Coloque novamente o sexo do bb")
        '''


'''

n  = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1 
print('Voce digitou {} numeros pares {} numeros impares'.format(par, impar))


'''


'''r = 'S'
while r == 'S':
    n = int(input("Digite um valor:"))
    r = str(input("Quer continuar? [S/N]")).upper()
print("FIM")'''
#algorito que leia o dobro de um numero e triblo e raiz quadrada

calculo = float(input("escreva seu numero parapoder saber seus resultados!"))

while calculo < 0:
    print("--ERRO--")
    calculo = float(input("escreva seu numero parapoder saber seus resultados!"))
    #add pq eu quis mesmo 

calcular_dobro = calculo * 2
calcular_triplo = calculo * 3
calcular_raizquadrada = calculo ** (1/2)

print(f"O dobro do numero é: {calcular_dobro}")
print(f"O triplo do numero escolido é:  {calcular_triplo}")
print(f"A raiz quadrada do numero escolido é {calcular_raizquadrada}")
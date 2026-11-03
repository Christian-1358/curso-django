from uteis22 import fatorial
import uteis22
#pode colocar import uteis 

num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f'O  fatorial de {num} é {fat}')


print(f' O dobro de {num} é {uteis22.dobro(num)}')

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f += c
        return f
    
def dobro(n):
    return n * 2

def triplo(n):
    return n * 3 


# NAO IREI FAZER NADA DA 22, POIS EU JA FASSO ISSO EM PROJETOS 

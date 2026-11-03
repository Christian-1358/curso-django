colocados = (
    'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 
    'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Júlia', 
    'Kleber', 'Larissa', 'Marcos', 'Natália', 'Otávio', 
    'Patrícia', 'Rafael', 'Sabrina', 'Thiago', 'Vanessa'
)

tabela = (input("Dejesa ver colocados, [S/N]".upper()))
if tabela == 'S' or tabela == "s":
    
    for futebolista in colocados:
        print(f'Futebolista: {futebolista}')
        print('=-'*20)
    else: 
        print(f"Primeiro 5 colocados:  {', '.join(colocados[:5])}")
        print(f"Os 4 ultimos colocados são: {', '.join(colocados[-4:])}")
        print(f"times por onrdem alfabetica: {sorted(colocados)}")
if tabela== 'N' or tabela == 'n':
        print(f"Os 5 primeiros são: {', '.join(colocados[:5])}")
        print(f"Os 4 ultimos colocados são:  {', '.join(colocados[-4:])}")
        print(f"times por onrdem alfabetica: {sorted(colocados)}")






'''lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezessei', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input("Digite um numero de 0 até 20: "))
    if 0 <= numero <= 20:
        break
    print("tentar novamente.", end='')
    continue


print(f"Seu numero escolido que foi tranformado por estenso é: {lista[numero]} ")'''
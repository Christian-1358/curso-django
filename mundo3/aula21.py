'''#101

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print("~" * tamanho)
    print(f"  {mensagem}")
    print("~" * tamanho)


# Exemplo de uso
escreva("Olá, Mundo!")

'''



'''#103
def ficha(jog="<desconhecido>", gol=0):
      print(f"O jogador {jog} marcou {gol} golo(s) no campeonato.")


# Programa principal
n = input("Nome do Jogador: ")
g = input("Número de Golos: ")

if g.isnumeric():
  g = int(g)
else:
  g = 0

if n.strip() == "":
  ficha(gol=g)
else:
  ficha(n, g)


'''


'''#104:

def leiaInt(msg):
  ok = False
  valor = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print("\033[0;31mErro! Digite um número inteiro válido.\033[m")
    if ok:
      break
  return valor


# Programa principal
n = leiaInt("Digite um n: ")
print(f"Você acabou de digitar o número {n}")
'''

'''#102




def fatorial(n, show=False):
      """-> Calcula o fatorial de um número.

  :param n: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do fatorial de n.
  """
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end="")
      if c > 1:
        print(" x ", end="")
      else:
        print(" = ", end="")
    f *= c
  return f


# Exemplo de uso
print(fatorial(5, show=True))'''
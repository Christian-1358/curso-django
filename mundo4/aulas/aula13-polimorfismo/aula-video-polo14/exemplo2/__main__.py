from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(200)
    
    c1 += 50
    c1 -= 10
    
    if (c1 == c2):
        print(" vcs tem o mesmo valor ")
    else:
        print("as carteira tem o valores diferentes")
    
    if (c1 <= c2):
        print("A segunda carteira tem mais dinheiro")
    else:
        print("A primeira cartei tem masi money")
    print(c1)
    print(c2)

if __name__ ==  '__main__':
    main()
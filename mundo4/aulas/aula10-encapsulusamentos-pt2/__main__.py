import rich
from aula10 import Avaliacoes



def main():
    av1 = Avaliacoes("chris", "portugues", )
    av1.nota = -231231
    print(f"{av1.nome} tirou {av1.nota} em {av1.diciplina}")
    rich.inspect(av1, private=True)


if __name__ == '__main__':
    main()
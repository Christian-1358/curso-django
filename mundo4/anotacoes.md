POO (brasil) = Programação orientada a objetos
OOP (ingles ) = Object oriented Program 



🧠 Conceitos-Chave ExplicadosDeclaração da Classe (class): 
  É o molde ou a planta baixa de um objeto. Define quais serão os atributos e métodos que os objetos criados a partir dela irão possuir.  

  Atributos:   Representam as características ou o estado do objeto (ex: nome, idade, saldo). São definidos dentro do construtor utilizando o self.   

  Métodos:   Representam as ações ou comportamentos que o objeto pode realizar (ex: calar(), depositar(), andar()).  

  Método Construtor (__init__): É executado automaticamente no momento em que um objeto é instanciado. Serve para inicializar os atributos do objeto. O parâmetro self     faz  referência à própria instância que está a ser criada.  

   Instanciação (obj = MinhaClasse()):   O processo de criar um objeto real (físico na memória) a partir do molde da classe.   





print(int.__doc__)


# DUNDER  = Double Underline __
# Docstring

# NA AULA5 :

class Gafanhoto:
     # Quando eu coloco """ eu crio uma Documentação, q com isso se eu colocar: print(g1.__doc__) ele ira mostrar a documentação da minha classe
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    
    Para criar uma nova pessoa, use:
    
    Variavel = Gafanhoto(nome, idade)
    
    """


    para poder coloar emogis usando rich, vc coloca no terminal> python -m rich.emoji



# O QUE SAO HERANÇAS (em classe):

herança, são classes dentro de outras classes com dados q vc pode colocar, 

ex: classe casa (class Casa), dentro da casa, vc sempra vai saber q vai ter paredes, e comodos, ent a classe casa, é o "esqueleTO '  e dentro da classe casa, vc pode criar classes "bebes" vc podera colocar classes dentro da classe mae

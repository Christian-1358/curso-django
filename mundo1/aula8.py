'''from random import randint

alunos = ["Alice", "Bob", "Charlie", "David"]

def sortear_pessoa():
    sortear = randint(1, 4 ) 
    print(f"alunos sorteado: {sortear} - {alunos[sortear-1]}")
    
          

print("Sorteando um aluno...")
 
sortear_pessoa()



'''
import pygame 

pygame.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()

print("precione enter para sair" ) 
pygame.mixer.stop()
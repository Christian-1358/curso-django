#95

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
        
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"cod":<4}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')


















'''
#94
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
        
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')

media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()

print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO')
'''







''''#93

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}: ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''




'''#92 : 

from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    # Calcula a idade de aposentadoria (idade atual + anos faltantes para completar 35 de contribuição)
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')


'''









'''#91
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

# Ordenando o dicionário por valores em ordem decrescente (maior para o menor)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)




'''



'''#90:
aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')'''
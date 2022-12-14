# -*- coding: utf-8 -*-
"""Python-comecando-com-a-linguagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sEDwYfNPALtanGdNIOiJ3LudxQf7LIHK

# Variáveis e Tipagem do Python

Uma variável só passa a existir quando atribuimos um valor, definindo assim o seu tipo.
"""

nome = 'Anne'
idade = 29
podeDirigir = True
saldo = 99,9

print(f'{nome} é do tipo: ', type(nome))
print(f'{idade} é do tipo: ', type(idade))
print(f'{podeDirigir} é do tipo: ', type(podeDirigir))
print(f'{saldo} é do tipo: ', type(saldo))

"""# Função print()

Função utilizada para imprimir algo na tela
"""

print('Olá')
print(29)

print('Brasil ganhou 5 titulos mundiais')
print('Brasil', 'ganhou', 5, 'titulos mundiais', sep='-')
print('Brasil', 'ganhou',5 , 'titulos mundiais', sep='')
print('Brasil', 'ganhou',5 , 'titulos mundiais', end='\n') #pular linha
print('Brasil', 'ganhou',5 , 'titulos mundiais', end='') #pular linha

pais = 'Itália'
quantidade = 4
print(pais, "ganhou", quantidade, 'titulos mundiais')

subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")

dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep='/')

"""# Comparando variáveis"""

print('***********************')
print('Bem vindo no jogo de adivinhação')
print('*********************** \n')

numero_secreto = 12
chute = input("Digite o seu numero: ")
print('Você digitou', chute)

if numero_secreto == int(chute):
  print('Você acertou! \n')
else:
  print('Você não acertou. \n')

print('Fim do jogo!')
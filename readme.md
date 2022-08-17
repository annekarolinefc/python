<h1>Aprendendo <b>Python</b></h1>
</br>
<h2>Links do Google Colab</h2>
<h3>Cursos realizados:</h3>
<a href="https://colab.research.google.com/drive/1fVTpY102py-6DGVqOT-IBIohjJlBp5IS?usp=sharing">Curso Python para Data Science</a></br>
<a href="https://colab.research.google.com/drive/1sEDwYfNPALtanGdNIOiJ3LudxQf7LIHK?usp=sharing">Curso Python: começando com a linguagem</a></br>
</br>
<h3>Listas de exercicios</h3>
<a href="https://colab.research.google.com/drive/1mulhE1JDlaDyOPNYVz4SC4PJeBrTM0_n?usp=sharing">Lista 01</a></br>
<a href="https://colab.research.google.com/drive/1JuTiwjZ9Oz2jF59r5h9Z33iE0xi-1uHK?usp=sharing">Lista 02</a></br>
</br>

# Exercícios – Parte 1

</br> 

## Exercício 1
Escreva um código Python que lê do teclado o nome e a idade de um usuário e imprime o ano em que o
usuário completará 100 anos.
Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.

```sh
import datetime

current_time = datetime.datetime.now()
ano_atual = current_time.year

nome = input('Insira seu nome: ')
idade = input('Insira usa idade: ')
idade = int(idade)
ano = 100-idade+2022;
print(f'{nome} irá completar 100 anos em {ano}.')
```
</br>

## Exercício 2
Escreva um código Python que lê do teclado um número digitado pelo usuário e imprime se ele par ou ímpar

```sh
numero = input('Digite um numero: ')
numero = float(numero)
if (numero%2==0):
  print(f'{numero} é par.')
else :
  print(f'{numero} é impar.')
```

<br>

## Exercício 3
Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
Dica: olhe a documentação da função range(). Mais informações no link

```sh
for numeros in range(0,21, 2):
  print(numeros)
```

<br>

## Exercício 4
Escreva um código Python que imprime todos os números primos de 0 até 100.

```sh
for numero in range(2, 101):
    for count in range(2, numero):
        if (numero%count) == 0:
            break 
    else:
        print(f'{numero} é primo')
```

<br>

## Exercício 5

```sh
dia = input('Insira o dia: ')
mes = input('Insira o mês: ')
ano = input('Insira o ano: ')

print(dia, mes, ano, sep=('/'))
```
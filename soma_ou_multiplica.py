'''
Crie um programa que lê um valor numérico N e que em seguida lê N números.
Armazene esses números em uma lista. Em seguida, leia do usuário 3 números
inteiros (OP, A e B). O primeiro número (OP) representa uma operação 
matemática (0 é soma, 1 é multiplicação) que deve ser realizada em cima
dos dois números cujas posições (1 a N) na lista são A e B. O programa
deve então apresentar a operação e seu resultado.

'''

quantidade_numeros = int(input('Qual o N? '))
print('Digite os valores: ')

lista_numeros = []

for i in range(0, quantidade_numeros):
  numero = int(input(''))
  lista_numeros.append(numero)
  
operacao = input('Qual a operação? ')
ordem_a = int(input('Qual o A? '))
ordem_b = int(input('Qual o B? '))

numero_a = lista_numeros[ordem_a-1]
numero_b = lista_numeros[ordem_b-1]

if operacao=='0':
  soma_a_b = numero_a + numero_b
  print('{} + {} = {}'.format(numero_a,numero_b,soma_a_b ))
  

if operacao=='1':
  multiplicacao_a_b = numero_a *numero_b
  print('{} * {} = {}'.format(numero_a,numero_b,multiplicacao_a_b ))
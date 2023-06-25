
# Escreva um programa que receba um número N para gerar
# os N primeiros termos da série de
# Fibonacci: 1, 1, 2, 3, 5, 8, 13, ...

quantidade=int(input('Digite o número N para gerar os N primeiros termos da série fibonacci: '))
lista_sequencia=[1,1]
numero=0
for i in range(1,quantidade,1):
    numero=numero+lista_sequencia[i-1]
    lista_sequencia.append(numero)

print(lista_sequencia)


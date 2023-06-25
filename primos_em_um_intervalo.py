# Escreva um programa que peça ao usuário dois números
# inteiros n1 e n2 (n2 > n1) e imprima quantos
# números primos existem no nintervalo [n1, n2],
# incluindo esses dois números.
# Lembre-se que um número é primo se ele é
# divisivel apenas por 1 e por ele mesmo.

num_1=int(input('n1: '))
num_2=int(input('n2: '))

if num_1>num_2 :
    aux=num_1
    num_1=num_2
    num_2=aux
quant_primos=0

for i in range(num_1,num_2+1,1):
  divisores=[]
  for j in range(1,i+1):
    if i%j==0:
        divisores.append(j)
  if len(divisores)==2:
    quant_primos=quant_primos+1
    
print('Existem {} numeros primos entre {} e {}'.format(quant_primos,num_1,num_2))
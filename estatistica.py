'''
Nesse contexto, crie um programa que lê um 
conjunto de N números (N > 2). Para isso, o programa 
deve primeiro ler o valor de N e depois a lista de N 
números reais (float). Os dados devem ser informados 
na ordem crescente, ou seja, do menor valor para o maior, 
podendo haver elementos repetidos. 

Em seguida, o programa deve realizar a análise dos dados mostrando as informações presentes 
em um boxplot (limite inferior, o 1º quartil, a mediana, o 3º 
quartil e o limite superior), considerando o seguinte:


'''

n = int(input('Qual o valor de N? '))
lista_numeros=[]

num_1 = int( input('Número 1 = ') )
lista_numeros.append(num_1)

for i in range(1,n,):
    num_1 = int(input('Número {} = '.format(i+1)))
    lista_numeros.append(num_1)
    num_anterior=lista_numeros[i-1]
    if num_anterior>num_1:
        print('Erro! Conjunto tem de estar em ordem crescente')
    
quartil_1 = lista_numeros[round(n * 1/4)-1]

if n%2==0:
    mediana= (lista_numeros[n//2]+lista_numeros[(n//2)-1])/2

elif n%2==1:
    mediana= lista_numeros[(n//2)]

quartil_3 = lista_numeros[round(n * 3/4)]

valor_max= max(lista_numeros)
while valor_max>mediana +(1.5*(quartil_3-quartil_1)):
      lista_numeros.remove(valor_max)
      valor_max= max(lista_numeros)

valor_min= min(lista_numeros)
while valor_min<mediana -(1.5*(quartil_3-quartil_1)):
      lista_numeros.remove(valor_min)
      valor_min= min(lista_numeros)


print('Limite inferior: {}'.format(valor_min))
print('1o quartil: {}'.format(quartil_1))
print('Mediana: {}'.format(mediana))
print('3o quartil: {}'.format(quartil_3))
print('Limite superior: {}'.format(valor_max))

'''
Escreva um programa que lê a quantidade dos alunos 
de uma turma. Em seguida, o programa deve ler os nomes 
de cada aluno e imprimí-los na ordem inversa.

'''


quantidade_alunos = int(input('Quantos nomes? '))
lista_alunos=[]
lista_alunos_invertida=[]
for i in range(0,quantidade_alunos):
  nome = input(f'Aluno {i+1}: ')
  lista_alunos.append(nome)

print('Nomes invertidos:' )
for j in range(-1,-quantidade_alunos-1,-1):
  print(lista_alunos[j])

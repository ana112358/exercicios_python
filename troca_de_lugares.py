'''
Em uma turma de alunos que conversavam muito, um professor montou 
a seguinte estratégia. Após os alunos se sentarem, ele mandava os 
alunos trocarem de lugar. Para ajudar esse processo, crie um programa
para ajudar esse professor. O programa deve ler um valor N, que 
representa a quantidade de alunos. Em seguida, deve ler os nomes 
de cada aluno. Considere a sequência lida como a ordem das cadeiras 
dos alunos. O programa deve então imprimir os nomes em uma nova ordem, 
trocando os alunos sentados em cadeiras de número par (o da primeira 
cadeira par vai para a última par, o da segunda para a antepenúltima, etc.).

Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, 
vão haver 3 cadeiras pares), o aluno da cadeira central não terá seu local trocado.

'''
quantidade_alunos = int(input('Quantos alunos?'))
lista_alunos = []

for i in range(0,quantidade_alunos):
    nome = input('aluno {} :'.format(i+1))
    lista_alunos.append(nome)

lista_pares_invertida=lista_alunos

if quantidade_alunos%2==0:
    for j in range(1,quantidade_alunos-1,2):
        nome_armazenado_1 = lista_alunos[j]
        nome_armazenado_2 = lista_alunos[-j]
        lista_alunos[j] = nome_armazenado_2
        lista_alunos[-j] = nome_armazenado_1

elif quantidade_alunos%2==1:
    indice_meio= ((quantidade_alunos-1)//2)
    nome_meio = lista_alunos[indice_meio]
    for j in range(1,quantidade_alunos-2,2):
        nome_armazenado_1 = lista_alunos[j]
        nome_armazenado_2 = lista_alunos[-j-1]
        lista_alunos[j] = nome_armazenado_2
        lista_alunos[-j-1] = nome_armazenado_1

print('NOVA LISTA: ')
for h in range(0, quantidade_alunos):
    print(lista_alunos[h])
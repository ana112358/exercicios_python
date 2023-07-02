'''

nome do jogador, os valores S, B e A, representam a
quantidade de tentativas de saques, bloqueios e ataques; 
os valores S1, B1 e A1, representando o número de saques, 
bloqueios e ataques deste jogador que tiveram sucesso.

'''
quantidade_jogadores = int(input('Quantidade de jogadores : '))
print('Digite os dados para cada jogador : ')
lista_nome=[]
lista_s=[]
lista_s1=[]
lista_b=[]
lista_b1=[]
lista_a=[]
lista_a1=[]
soma_saques = 0
soma_bloqueios= 0
soma_ataques= 0
soma_saques_sucesso= 0
soma_bloqueios_sucesso= 0
soma_ataques_sucesso= 0

for i in range(1,quantidade_jogadores+1):
    nome = input('Nome:')
    saques = int(input('Saques: '))
    bloqueios = int(input('Bloqueios: '))
    ataques = int(input('Ataques: '))
    saques_sucesso = int(input('Saques de sucesso: '))
    bloqueios_sucesso = int(input('Bloqueios de sucesso: '))
    ataques_sucesso = int(input('Ataques de sucesso: '))
    lista_nome.append(nome)
    lista_s.append(saques)
    lista_s1.append(saques_sucesso)
    lista_b.append(bloqueios)
    lista_b1.append(bloqueios_sucesso)
    lista_a.append(ataques)
    lista_a1.append(ataques_sucesso)
         
for j in range(0, quantidade_jogadores):
    soma_saques += lista_s[j]
    soma_bloqueios+= lista_b[j]
    soma_ataques+= lista_a[j]
    soma_saques_sucesso+= lista_s1[j]
    soma_bloqueios_sucesso+= lista_b1[j]
    soma_ataques_sucesso+= lista_a1[j]

pontos_saque= (soma_saques_sucesso/soma_saques)*100
pontos_bloqueio= (soma_bloqueios_sucesso/soma_bloqueios)*100 
pontos_ataque= (soma_ataques_sucesso/soma_ataques)*100
print('As estatísticas do jogo são as seguintes:')
print('Pontos de Saque: {:.2f} %'.format(pontos_saque))
print('Pontos de Bloqueio: {:.2f} %'.format(pontos_bloqueio))
print('Pontos de Ataque: {:.2f} %'.format(pontos_ataque))
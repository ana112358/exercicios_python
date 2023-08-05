# Exercício - Sistema de Perguntas e respostas
# Treinando o uso de dicionários no python
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos=0 
erros=0 
for pergunta in perguntas:
    dicionario_atual = pergunta
    print(dicionario_atual['Pergunta'])
    for opcao in enumerate(dicionario_atual['Opções']):
        print(opcao[0], '|', opcao[1])
        
    resposta = input('Resposta: ')
    if resposta.isdigit():
        resposta = int(resposta)
    
    
    lista_opcoes = dicionario_atual['Opções']
    qtd_opcoes= len(lista_opcoes)     
    if resposta is not None:
        if resposta>=0 and resposta< qtd_opcoes:    
            if lista_opcoes[resposta] == dicionario_atual["Resposta"]:
                print('IUPPP, VOCÊ ACERTOU !!!')
                acertos+=1
            else:
                print('QUE PENA, :(. VOCÊ ERROU !!!')
        else:
            break
    else:
        break
if resposta is not None:
    if resposta>=0 and resposta< qtd_opcoes:  
        print('VOCÊ ACERTOU ', acertos, '/ 3')
    

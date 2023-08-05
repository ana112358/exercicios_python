import os;
lista_compras = []

while True:
    opcao = input('[a]dcionar, [r]etiras, [listar]: ')
    if opcao == 'a' :
        os.system('cls')
        adc_item = input('Adicionar: ')
        lista_compras.append(adc_item)
    elif opcao== 'r':
        try:
            os.system('cls')
            indice= int(input('Qual indice deseja retirar: '))
        except ValueError:
            print('Digite um número inteiro')
            continue
        if indice < 0 or indice >= len(lista_compras):
            print('O índice não existe na lista')
            continue

        lista_compras.pop(indice)
    elif opcao=='l':
        os.system('cls')
        for i, valor in enumerate(lista_compras):
            print(f'{i} {valor}')
    elif opcao =='parar':
        break
    else:
        print('Digite [a], [r], [l] ou [sair]')


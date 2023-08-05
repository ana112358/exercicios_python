import random

for _ in range(100):
    cpf_usuario = ''
    for i in range(9):
        cpf_usuario +=str(random.randint(0,9))

    soma_geral=0
    for i in range(9):
        dig_cpf_atual = int(cpf_usuario[i])
        numero = 10-i
        soma_atual = dig_cpf_atual * numero
        soma_geral += soma_atual
    # soma_geral = soma de todos os resultados 

    resto_11 = (soma_geral *10)%11
    dig_1_cpf = 0 if resto_11 >9 else resto_11

    cpf_adc = cpf_usuario[:9] + str(dig_1_cpf)

    soma_geral = 0

    for i in range(0,10):
        dig_cpf_atual = int(cpf_adc[i])
        numero = 11-i
        soma_atual = dig_cpf_atual * numero
        soma_geral += soma_atual
    # soma_geral = soma de todos os resultados 

    resto_11 = (soma_geral *10)%11 

    dig_2_cpf = 0 if resto_11 >9 else resto_11

    cpf_novo = cpf_usuario[:9]+str(dig_1_cpf) +str(dig_2_cpf)


    print(f'CPF: {cpf_novo}')
    
    
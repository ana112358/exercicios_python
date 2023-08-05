"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

entrada=input('CPF: ')
cpf_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)
entrada_e_sequencial=entrada == entrada[0]*len(entrada)
if entrada_e_sequencial:
    print('Você digitou dados sequenciais!')
    sys.exit()

soma_geral=0

for i in range(0,9):
    dig_cpf_atual = int(cpf_usuario[i])
    numero = 10-i
    soma_atual = dig_cpf_atual * numero
    soma_geral += soma_atual
   
# soma_geral = soma de todos os resultados 

resto_11 = (soma_geral *10)%11

dig_1_cpf = 0 if resto_11 >9 else resto_11


cpf_adc = cpf_usuario[:9] +str(dig_1_cpf)
print(cpf_adc)
soma_geral = 0
for i in range(0,10):
    dig_cpf_atual = int(cpf_adc[i])
    numero = 11-i
    soma_atual = dig_cpf_atual * numero
    soma_geral += soma_atual
    print(dig_cpf_atual, numero, sep='-')
# soma_geral = soma de todos os resultados 

resto_11 = (soma_geral *10)%11 

dig_2_cpf = resto_11 if resto_11 <=9 else 0
print(dig_2_cpf)

cpf_novo = cpf_usuario[:9]+str(dig_1_cpf) +str(dig_2_cpf)

verificacao= 'Valido' if cpf_usuario==cpf_novo else 'Invalido'

print(f'O CPF {cpf_usuario} é {verificacao}')
    
    
# Um número inteiro positivo,n, é dito triangular se,
# e somente se, ele é o resultado do produto de
# três números inteiros positivos e consecutivos.
# Escreva um algoritmo que leia um número inteiro
# positivo, n, e escreva como saída “é triangular”
# se n for triangular e “não é triangular”, caso contrário.


num= int(input('Número inteiro positivo: '))

triangular=False
for i in range(1,num):
    terna= (i-1)*i*(i+1)
    if terna == num :
        triangular=True

if triangular==True:
    print(num, ' é triangular ')
else:
    print(num, ' não é triângular ')
    

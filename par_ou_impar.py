def par(numero):
    if numero%2==0:
        return True
    else:
        return False

num = int(input('Número:'))
num_par = par(num)
if num_par == True:
    print(f'{num} é par '  ) 
else:
     print(f'{num} é ímpar '  ) 

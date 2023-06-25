#Crie um programa que leia um número N (0<N<10)
#e que imprima uma sequência de números .

num=0
while num>9 or num<1:
   num= int(input('Número ente 0 e 10 :'))

for i in range(1,num+1):
    print(str(i)*i)
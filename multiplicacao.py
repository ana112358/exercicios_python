def multiplicar(*arg):
    multiplicacao =1
    for num in arg:
        multiplicacao= multiplicacao* num
    return multiplicacao


resultado = multiplicar(1,2,3,4,5)
print(resultado)
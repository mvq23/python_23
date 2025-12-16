def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 3)
suma(2, 3, 5, 7)
suma(2, 3, 5, 12, 1)

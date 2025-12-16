# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

# Fibonacci
# a, b = 0, 1
# while a < 100:
#     print(a)
#     a, b = b, a + b


# comando = ''
# while comando.lower() != 'salir':
#     comando = input('$ ')
#     print(comando)


while True:
    comando = input('$ ')
    print(comando)
    if comando.lower() == 'salir':
        break

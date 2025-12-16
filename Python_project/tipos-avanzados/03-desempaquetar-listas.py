numero = [1, 2, 3]

# queda feo
# primero = numero[0]
# segundo = numero[1]
# tercero = numero[2]

# print(primero,segundo, tercero)

primero,segundo, tercero = numero
print(primero,segundo, tercero)

numero = [1,2,3,4,5,6,7,8,9]
primero, segundo, *otros = numero
print(primero, segundo, otros)

primero, *otros, ultimo = numero
print(primero, ultimo, otros)

primero, segundo, *otros, penultimo, ultimo = numero
print(segundo, penultimo, otros)
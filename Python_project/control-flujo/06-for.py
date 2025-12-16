# for numero in range(5):
#     print(numero, numero * " Mariano ")

buscar = 103
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado:", buscar)
        break
else:
    print("no esta")

for char in "Don gato":
    print(char)

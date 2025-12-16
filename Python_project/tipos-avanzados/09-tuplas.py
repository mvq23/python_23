numeros = (1,2,3) + (4,5,6)
print(numeros)

punto = tuple([1,2])
print(punto)

menosNumeros = numeros[:4]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero,segundo,otros)

#iterar
for n in numeros:
    print(n)

#las tuplas no se modifican para ello pasa a lista y ahi se modifica
listasNumeros = list(numeros)
listasNumeros[0] = "modifico"

print(listasNumeros)
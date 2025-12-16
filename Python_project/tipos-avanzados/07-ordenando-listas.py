numeros = [1,20,3,14,5,16,7,18,9]

#numeros.sort(reverse=True)

numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [["sol",4], 
            ["andy",1],
            ["mariano",5],
            ["mari",3]]

def ordena(elementos):
    return elementos[1]

usuarios.sort( key=ordena, reverse=True)
print(usuarios)

# manera correcta

usuarios.sort( key=lambda elemento: elemento[1])
print(usuarios)
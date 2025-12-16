# una coleccion de datos que se encutran agrupados por una llave y un valor
# distintas formas para acceder a los diccionarios

punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto ["z"] = 45
punto ["lala"] = 12
print(punto)

if "lala" in punto:
    print("si esta lala", punto["lala"])

print(punto.get("q"))
print(punto.get("q", 0)) # Poner un valor por defecto sino existe

print(punto.get("lala",97)) #existe muestra el que tiene el indice

del punto ["x"] # elimina llave en conjunto con su valor
del (punto ["y"]) # funcion del elimina una llave asociada el diccionario

print (punto)

punto["x"] = 25

# iterar todas las llaves dentro de su valor, devuelve todas las llaves que tiee asociado ese diccionario
# llamar al diccionario y pasarle el valor como []
print ("ultimo")
for valor in punto:
    print (valor, punto[valor])

# otra forma y en este caso devuelve tuplas
for valor in punto.items():
    print(valor)

# si desempaquedamos la tupla
for llave, valor in punto.items():
    print(llave,valor)

# uso realista de los diccionarios
usuarios = [
    {"id":1, "nombre": "juan"},
    {"id":2, "nombre": "pedro"},
    {"id":3, "nombre": "mariano"},
    {"id":4, "nombre": "andrea"}
]

for usuario in usuarios:
    print(usuario ["nombre"])
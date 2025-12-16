usuarios = [["sol",4], 
            ["andy",1],
            ["mariano",5],
            ["mari",3]]

# nombres = []
# for usuarios in usuarios:
#     nombres.append(usuarios[0])
# print(nombres)

#(variable = [expresion for item in items])

#Transformar 
#map
#nombres = [usuario[0] for usuario in usuarios]

#Filtrar
#filter
#nombres = [usuario for usuario in usuarios if usuario[1]>0]

#Filtrar y Transformar
#nombres = [usuario[0] for usuario in usuarios if usuario[1]>0]

#print(nombres)

# funciones map filter son programacion funcional es lo mismo que usar comprension de listas depende de cada uno.
#nombres = list(map(lambda usuario: usuarios[0], usuarios))

menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosusuarios)
#set significa grupo o conjunto

primer = {1,1,2,2,3,4}
# primer.add(5)
# print(primer)
# primer.remove(1)
# print(primer)

segundo = [2,4,5]
# pasar lista a set
segundo = set(segundo)
print(segundo)

# union (al ser un set elimina los duplicados)
print(primer | segundo)

# interseccion
print(primer & segundo)

# diferencia se muestra lo de le la izquierda restando los de la derecha y los que esten en ambos
print(primer - segundo)

# diferencia simetrica los que no estan en uno y el otro
print(primer ^ segundo)

# los sets no se encuentra ordenados por lo cual no se puede acceder con [1]

if 5 in segundo:
    print("Si esta")
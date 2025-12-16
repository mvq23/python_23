pila = []
#agregar elementos a la pila
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

#borrar el ultimo elemento
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)

#acceder al ultimo elemento de la pila
print(pila[-1])
ultimoElemento = pila.pop()
ultimoElemento = pila.pop()
if not pila:
    print("pila vacia")
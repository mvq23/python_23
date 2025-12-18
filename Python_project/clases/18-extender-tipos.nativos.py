#Funciona correctamente pero no es la mas recomendada y legible
#lista = list([1, 2, 3])

#lista.append(4)
#lista.insert(0, 0)
#print(lista)  # Salida: [0, 1, 2, 3, 4]

#Extender tipos nativos
class Lista(list):
    def prepend(self, valor):
        self.insert(0, valor)

lista = Lista([1, 2, 3])
lista.append(4)
lista.prepend(0)

print(lista)  # Salida: [0, 1, 2, 3, 4]
#por definición y buenas practicas no se usan variables globales.
saludo = "hola a todos"

def saludar():
    global saludo #asi se haria pero no se debe hacer no es una buena práctica
    saludo = "hola gil"

def saludaMono():
    saludo = "hola monooooo"
    print(saludo)

print (saludo)
saludar()
print (saludo)
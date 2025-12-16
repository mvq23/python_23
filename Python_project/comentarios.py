"""
Este archivo es un ejemplo de docstring de módulo.
Sirve como documentación, no como comentario.
"""


def saludar(nombre):
    """Esta función saluda a la persona por su nombre"""
    return f"Hola, {nombre}"


print(saludar("Mariano"))
print(saludar.__doc__)  # mostramos el docstring de la función
print(__doc__)          # mostramos el docstring del módulo

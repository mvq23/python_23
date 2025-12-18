class Usuario():
    def guardar(self):
        print("Guardando usuario en la base de datos")

class Sesion():
    def guardar(self):
        print("Guardando sesión en archivo")

def guardar(entidades):#entidad es una lista
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion()   

guardar([usuario, sesion])

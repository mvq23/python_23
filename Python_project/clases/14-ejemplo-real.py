class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error: tienes que definir la 'tabla'")

    def guardar(self):
        print(f"Guardando {self.tabla} en la base de datos")

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando en la tabla {self.tabla} el registro con id {id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "usuarios"

usuario = Usuario()
usuario.guardar()   
usuario.buscar_por_id(2310)
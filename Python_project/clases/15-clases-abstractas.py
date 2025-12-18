from abc import ABC, abstractmethod

class Model(ABC):
    
    @property
    @abstractmethod
    def tabla(self):
        pass
   
    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando en la tabla {self.tabla} el registro con id {id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "tabla_usuarios"

    def guardar(self):
        print(f"Guardando {self.tabla} en la base de datos")

Usuario = Usuario() 
Usuario.guardar() 
Usuario.buscar_por_id(2310)
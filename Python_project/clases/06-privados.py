class Perro:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):  
        print(f"{self.__nombre} dice Hello!!!")

    @classmethod
    def factory(cls):
        return cls("Tao", 4)

perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
#contiene todas las propiedades que tiene una instancia de un objeto
#devuelve: _NombreClase__nombreProp
print(perro1.__dict__) 
#podemos mostrarlo
print(perro1._Perro__nombre)
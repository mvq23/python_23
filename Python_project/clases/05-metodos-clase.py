class Perro:
    #propiedad de clase
    patas = 4

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # cls es para referirse a la clase misma
    @classmethod
    def habla(cls):  
        print("Hello!!!")

    @classmethod
    def factory(cls):
        return cls("Tommy", 4)

Perro.habla()
perro1 = Perro("Tao", 8)
perro2 = Perro("Pipo", 4)
perro3 = Perro.factory()

print(perro3.nombre, perro3.edad)
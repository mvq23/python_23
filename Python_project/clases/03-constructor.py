class Perro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: HI!!!")

mi_perro = Perro("Tao", 10)
mi_perro.habla()
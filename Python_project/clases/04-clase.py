class Perro:
    #propiedad
    patas = 4

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: HI!!!")

Perro.patas = 3
mi_perro = Perro("Tao", 10)
mi_perro.patas = 5
mi_perro2 = Perro("Tao_2", 10)

print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)


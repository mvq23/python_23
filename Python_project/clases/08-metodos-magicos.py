# Metodo que se va a ejecutar cuando no lo hemos llamado en este caso el constructor
# https://rszalski.github.io/magicmethods/
# https://rszalski.github.io/magicmethods/#representations

class Perro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chau perrit {self.nombre}")

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: HI!!!")

perro = Perro("Pipo",7)
#print (perro)
#texto = str(perro)
#print (texto)
del perro
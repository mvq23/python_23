# tratar de que la herencia no sea mas de uno o dos niveles

class Animal:
    def comer(self):
        print("Comiendo")
    
class Perro(Animal):
    def pasear(self):
        print("Paseando")
        
class Gato(Perro):
    def saltar(self):
        print("Saltando")
        
perro = Perro()
gato = Gato()
gato.comer()
perro.pasear()

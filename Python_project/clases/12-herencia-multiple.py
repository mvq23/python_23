
class Animal:
    def comer(self):
        print("Comiendo")
    
class Perro:
    def pasear(self):
        print("Paseando")
        
class Gato(Perro,Animal): #herencia multiple
    def saltar(self):
        print("Saltando")

gato = Gato()
gato.comer()

print("-----------------------------------")

# hereda de derecha a izquiera y puede ser un problema si se altera el orden en que lo hereda otra clase
class Animal:
    def comer(self):
        print("Comiendo")
        
    def pasear(self):
        print("Paseando animales")
        
class Perro:
    def pasear(self):
        print("Paseando al perro")

class Gato(Perro,Animal): #herencia multiple
    def saltar(self):
        print("Saltando")
        
gato = Gato()
gato.pasear()

print("-----------------------------------")

class Gato(Animal,Perro): #herencia multiple
    def saltar(self):
        print("Saltando")
        
gato = Gato()
gato.pasear()

print("-----------------------------------")

class Caminador:
    def caminar(self):
        print ("caminando")
        
class Volador:
    def volar(self):
        print ("volando")

class Nadador:
    def nadar(self):
        print ("nadando")

# intentar que las clases tengan sentido
class PezVolador(Volador,Nadador):
    def pezVolador(self):
        print ("El pez volador nada y vuela cuando salta fuera del agua")
        
class Pato(Volador,Nadador,Caminador):
    def pato(self):
        print ("El pato vuela, nada y camina")
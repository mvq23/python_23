class Ave:
    def __init__(self):
        self.volador = "Volador"

    def volar(self):
        print ("El ave está volando")

class Pato(Ave):
    def __init__(self):
        super().__init__() #para llamar al constructor de la clase padre
        self.nadador = "Nadador"
    
    def volar(self):     
       print ("El pato está volando")


pato = Pato()
pato.volar()
print (pato.volador, pato.nadador)
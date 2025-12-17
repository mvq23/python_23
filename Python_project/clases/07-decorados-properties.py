class Perro:
    def __init__(self,nombre):
        self. nombre = nombre
    
    @property #decorador, solo lo usamos para funciones que vsan a devolver un getter
    def nombre(self):
        print("Debugin para saber que paso por getter")
        return self.__nombre

    @nombre.setter #decorador que se usa para los set y es para que solo muestr
    def nombre(self,nombre):
        print("Debugin para saber que paso por setter")
        if nombre.strip():
            self.__nombre = nombre
        return
    
    #No lo usamos de esta manera mejor con @property y para seter usamos el nomebre de la propiedad .setter
    #esto para que no proponga estos metodos en herramientas de autocompletado y en nuestra terminal, no se puedna utilizar directamente
    #se los llama decoradores. El get_ y set_ no se usan y el constructor tambien se cambia igualando 
    #def get_nombre(self):
    #    return self.__nombre
    

perro = Perro("pipo")
print(perro.nombre)
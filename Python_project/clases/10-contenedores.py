class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"
    
class Categoria:
    productos = []
    
    def __init__(self,nombre,productos):
        self.nombre = nombre
        self.productos = productos
        
    def agregar(self,producto):
        self.productos.append(producto)
        
    def imprimir(self):
        for producto in self.productos:
            print(producto)
 
kayak = Producto("kayak",230)
bici = Producto("Bici",1230)
balon = Producto("Balon",30)
deportes = Categoria("Deportes", [kayak,bici])

deportes.agregar(balon)

deportes.imprimir()
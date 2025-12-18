# se usa para crear excepciones personalizadas con mas logica o informacion

class MiError(Exception):
    """Clase base para nuestras excepciones personalizadas"""
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"

def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por cero", 840)
    return 5/n
try:
    division()
except MiError as e:
    print(e.codigo)
    print(e.mensaje)
    print(e)
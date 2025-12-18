## tipos de excepciones
## https://docs.python.org/3/library/exceptions.html

## Las excepciones son costosas en terminos de rendimiento
## No se recomienda usarlas en bloques de codigo que se ejecutan con frecuencia

def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5/n
try:
    division()
except ZeroDivisionError as e:
    print(e)
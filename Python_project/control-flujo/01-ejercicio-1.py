mensaje = """
>>>>>>Calculeitor PRO 840<<<<<<
Las operaciones que puedes realizar son SUM, MULT, DIV y REST
Para salir ingresa la palabra 'Salir'
"""

print(mensaje)

res = ''

while True:
    if not res:
        res = input('Ingresa un numero: ')
        if res.lower() == 'salir':
            break
        res = int(res)
    oper = input('Ingrese operación: ')
    if oper.lower() == 'salir':
        break
    n2 = input('Ingresa el otro numero: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)
    if oper.lower() == 'sum':
        res += n2
    elif oper.lower() == 'mult':
        res *= n2
    elif oper.lower() == 'div':
        res /= n2
    elif oper.lower() == 'rest':
        res -= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es {res}")

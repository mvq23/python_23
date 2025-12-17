from pprint import pprint
string = "hola salame como andas?"

#funcion que se encarga de quitar los espacios
def quita_espacios(texto):
    return [char for char in texto if char != " "]

def cuenta(lista):
    chars_dict ={}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] =1
    return chars_dict
    
def ordena (dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )

def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_msj(diccionario):
    mensaje="Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- '{key}' con {valor} repeticiones. \n"
    return mensaje

sin_espacio = quita_espacios(string)
contados = cuenta(sin_espacio)
ordernados = ordena(contados)
mayores = mayores_tuplas(ordernados)
mensaje = crea_msj(mayores)
#pprint (contados, width=1)
print(mensaje)

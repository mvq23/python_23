from pprint import pprint
string = "hola salame de donde sos"

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
    

sin_espacio = quita_espacios(string)
contados = cuenta(sin_espacio)
pprint (contados, width=1)


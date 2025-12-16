def no_espacio(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def invertir(texto):
    texto_invertido = ""
    for char in texto:
        texto_invertido = char + texto_invertido
    return texto_invertido

def es_palindromo(texto):
    texto = no_espacio(texto)
    invertido = invertir(texto)
    if texto.lower() == invertido.lower():
        print("Es palindromo")
    else:
        print("No es palindromo")

es_palindromo("amo la paloma")
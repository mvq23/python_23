import requests
from random import choice
from colorama import Fore, Style
# Colores para los print sin usar COLORAMA
red_text = "\033[91m"  # Texto rojo
green_text = "\033[92m"  # Texto verde
reset_color = "\033[0m"  # Resetear los estilos de color

# Realiza una solicitud GET a la API
response = requests.get('https://clientes.api.greenborn.com.ar/public-random-word')

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtén los datos de la respuesta en formato JSON
    data = response.json()

    # Imprime las palabras obtenidas
    for word in data:
        guess = (word)
else:
    print('No se pudo obtener los datos. Código de estado:', response.status_code)

valid_letters = []
wrong_letters = []
attempts = 6
hits = 0
game_over = False

# Cuento la cantidad de letras unicas
def select_words (guess):
    select_word = guess
    unique_letters = len(set(select_word))

    return select_word, unique_letters

#Pido al usuario que ingrese una letra
def ask_for_a_letter ():

    chosen_letter = ''
    valid_letter = False
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'

    # Valido que la letra este en la palabra
    while not valid_letter:
        chosen_letter = input("Ingrese una letra: ").lower()
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            valid_letter = True
        else:
            print("La letra no esta en la palabra")

    return chosen_letter

# Nuevo tablero porque se crea cada vez que se elige una letra nueva
def show_new_board (select_word):

    hidden_list = []

    for l in select_word:
        if l in valid_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list).upper())

def check_letter(chosen_letter, hidden_word, lives, coincidences):

    end = False

    if chosen_letter in hidden_word:
        valid_letters.append(chosen_letter)
        coincidences += 1
    else:
        wrong_letters.append(chosen_letter)
        lives -= 1
    if lives == 0:
        end = lose()
    elif coincidences == unique_letters:
        end = win(hidden_word)

    return lives,end,coincidences

def lose():

    print(Fore.RED + "Te has quedado sin vidas." + Style.RESET_ALL)
    print("La palabra correcta era: " + hidden_word.upper())

    return True

def win(discovered_word):
    show_new_board(discovered_word)
    print(Fore.LIGHTBLUE_EX + "GANASTE!!! Has adivinado la palabra!!!" + Style.RESET_ALL)
    return True

hidden_word, unique_letters = select_words(guess)

while not game_over:
    print('\n' + '*' * 40 + '\n')
    show_new_board(hidden_word)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(wrong_letters).upper())
    if attempts == 1:
        print(Fore.RED + "¡Cuidado! Te queda 1 vida." + Style.RESET_ALL)
    else:
        print(f'Vidas: {attempts}')
    print('\n' + '*' * 40 + '\n')

    coincidences = 0 # Reinicia el contador de coincidencias
    letter = ask_for_a_letter()
    attempts, finished, hits = check_letter(letter, hidden_word, attempts, hits)

    # Actualizo la palabra oculta después de cada intento
    hidden_word, _ = select_words(guess)
    game_over = finished
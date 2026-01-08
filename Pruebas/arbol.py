from turtle import *
from colorsys import *

# Configuración inicial
tracer(100)
bgcolor('#0a1929')
hideturtle()
speed(0)

# Posición inicial
left(90)
up()
goto(0, -250)
down()

def draw(length, depth):
    # Caso base: hojas
    if length < 12:
        color(hsv_to_rgb(0.8, 1.0, 1.0))
        dot(4)
        return

    # Color según profundidad
    hue = (0.05 + depth * 0.02) % 1.0
    color(hsv_to_rgb(hue, 0.9, 0.8))

    # Grosor de la rama
    pensize(max(1, length / 12))

    # Rama principal
    forward(length)

    # Rama derecha
    right(30)
    draw(length * 0.7, depth + 1)

    # Rama central
    left(60)
    draw(length * 0.7, depth + 1)

    # Rama izquierda
    right(30)
    draw(length * 0.7, depth + 1)

    # Volver atrás
    backward(length)

# Dibujo inicial
draw(150, 0)
done()

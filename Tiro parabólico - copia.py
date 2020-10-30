# A00826973 Ingrid Giselle Paz Ramírez
# A00827533 Leo Abraham Puente Rangel
# Programa de un juego que consiste en lanzar bolas
# pequeñas que deben impactar en otras más grandes
# para desaparecerlas
# Fecha de entrega: 30/10/2020

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
#Posición de la pelota
speed = vector(0, 0)
#Velocidad
targets = []
#Puntos objetivo

def tap(x, y):
     #La velocidad depende del lugar en el que toque la pantalla
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        #Velocidad inicial x
        ball.y = -199
        #Velocidad inicial y
        speed.x = (2*x + 200) / 25
        #Velocidad en x
        speed.y = (2*y + 200) / 25
        #Velocidad en y

def inside(xy):
    #Verifica que los objetivos se encuentren en la pantalla
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    #Dibujar la pelota y objetivos
    "Draw ball and targets."
    clear()

    for target in targets:
        #Tamaño y color de los objetivos
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        #Tamaño y color de la pelota
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        #Movimiento aleatorio de los objetivos
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        #Movimiento de los objetivos hacia la izquierda
        target.x -= 0.5

    if inside(ball):
        #Movimiento de la pelota
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    #genera más objetivos
    targets.clear()

    for target in dupe:
        # Movimiento de los objetivos
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        #Los objetivos se detienen
        #al llegar al extremo de la ventana
        if not inside(target):
            goto(target.x, target.y)

    ontimer(move, 25)
    #Velocidad de los objetivos

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
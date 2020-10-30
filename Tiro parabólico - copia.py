# A00826973 Ingrid Giselle Paz Ramírez
# A00827533 Leo Abraham Puente Rangel
# Programa de un juego que consiste en lanzar bolas
# pequeñas que deben impactar en otras más grandes
# para desaparecerlas
# Fecha de entrega: 30/10/2020

# Llama funciones importantes de bibliotecas
from random import randrange
from turtle import *
from freegames import vector

# Define donde inicia el proyectil que es lanzado
ball = vector(-200, -200)
# Inicialmente el proyectil no tiene velocidad
speed = vector(0, 0)
# Conjunto vacío de objetivos
targets = []

# Se muestra la entrada y cálculo de la velocidad
# tomando en cuenta donde pulsa sobre la pantalla
# el jugador
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (2*x + 200) / 25
        speed.y = (2*y + 200) / 25

# Confirma que algo está dentro del rango de pantalla
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Parte del código que inicia a dibujar los objetivos
def draw():
    "Draw ball and targets."
    clear()
    # Dibujar nuevas bolas azules
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    # Desaparecer objetivo en caso de  "atinarle",
    # es decir, ocupar el mismo espacio de pantalla
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Define donde aparece cada objetivo (mismo lado
# pero diferente altura)
def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
    
    # Velocidad a la que mueven los objetivos
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            goto(target.x, target.y)

    ontimer(move, 25)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

# Final
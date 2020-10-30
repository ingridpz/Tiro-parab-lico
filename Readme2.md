# Readme Tiro Parabólico
> Modificación del juego Cannon.
El juego consiste en el lanzamiento de un proyectil hacia objetivos que recorren la pantalla
de derecha a izquierda, el objetivo es eliminar la mayor cantidad de objetivos. El juego termina 
cuando uno de estos objetivos llega al lado izquierdo de la pantalla. En este repositorio se modifica 
el juego de manera que el nivel de dificultad y la duración del juego sean mayores.

## Configuración incial
El videojuego utiliza funciones desde las bibliotecas random, turtle y freegames

```shell
from random import randrange
from turtle import *
from freegames import vector
```

Randrange permite elegi un número dentro de un rango de forma aleatoria, mientras que vector
cre un vector de dos dimensiones.
Al inicio del programa se establecen los vectores de posición y velocidad usando algunas 
de estas funciones.

## Desarrollo

La primera función descrita en el proyecto es la función tap, que relaciona la velocidad
con el lugar en el que el jugador toca la pantalla. La modificación realizada fue aumentar la velocidad
tanto vertical como horizontal del proyectil.  La función modificada ha quedado de esta manera:

```shell
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
```
En donde la posición en x y en y se ha multiplicado por dos. Esto ocasiona que el proyectil disparado
se mueva más rápido y alcance una altura mayor en menos timepo. Otra modificación ha sido en el uso de 
la función ontimer(), en la que el segundo argumento es el tiempo en el que se debe aplicar la funcion
introducida en el primer argumento. Al cambiar el tiempo en milisegundos en el que se debía aplicar la 
función move(), los objetivos azules se mueven más rápido de un lado de la pantalla a otro.
Por último se utilizó la función goto() para que el juego continuara a pesar de que los objetivos salieran
de la pantalla.

## Características

Para poder utilizar el videojuego de forma adecuada considere:
* Es necesario instalar la extensión freegames, de otra forma no funcionará.
* Considera que el juego no termina en determinado momento, el jugador decide cuando acabarlo.
* El código ahora se encuentra documentado para el entendimiento de las funciones usadas y definidas

## Contributing
Para la modificación del código original se utilizó además de Github Desktop, la herramienta Thonny

## Licencia

TFinalmente, cabe destacar que el código original fue obtenido de una página legal de Python (Grant Jenks) 
que distribuye este contenido para que le sea útil a quienes desarrollan proyectos similares a este.
Se comienda visitar:
http://www.grantjenks.com/docs/freegames/cannon.html


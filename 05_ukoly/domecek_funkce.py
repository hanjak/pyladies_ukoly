from turtle import forward, right, left, exitonclick,penup,pendown
from math import sqrt

strana = 30

def domecek (strana):
    "nakresli domecek o delce zadane strany"
    from turtle import forward, right, left, exitonclick,penup,pendown
    from math import sqrt
    left (90)
    forward (strana)
    right (90)
    forward (strana)
    right (90)
    forward (strana)
    right (90)
    forward (strana)
    right (135)
    forward (sqrt(2)*strana)
    left (90)
    forward ((sqrt (2)*strana)/2)
    left (90)
    forward ((sqrt (2)*strana)/2)
    left (90)
    forward (sqrt (2)*strana)
    left (45)

    exitonclick ()

domecek (90)

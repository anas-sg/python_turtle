from turtle import *

Screen().setup(width = 1.0, height = 1.0)
t = Turtle()
bgcolor("black")
t.color("white")
t.speed(0)
t.st()

L = 300
ANGLE = 170

for i in range(1000):
    t.fd(L)
    t.lt(ANGLE)

done()
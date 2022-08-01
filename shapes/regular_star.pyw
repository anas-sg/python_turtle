from turtle import *
from itertools import combinations, permutations 

L = 50
VERTICES = 5
ANGLE = 360 / VERTICES
INT_ANGLE = 180 - 2 * ANGLE
t = Turtle()
bgcolor("black")
t.color("yellow")
t.dot()
t.pd()
t.color("white")

def draw_star(height, centre=None):
    t.pu()
    if centre:
        t.goto(centre)
    t.seth(90)
    t.fd(height / 2)
    t.seth(270)
    t.lt(INT_ANGLE / 2)
    t.pd()
    for _ in range(VERTICES):
        t.fd(height)
        t.rt(2 * ANGLE)
        t.dot()

draw_star(500)
done()

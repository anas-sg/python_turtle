'''
A Python script that draws the Ghana flag centred at origin following the
technical specifications given by:
https://upload.wikimedia.org/wikipedia/commons/f/ff/Flag_of_Ghana_%28construction_sheet%29.svg
with some slight adjustments
'''
from turtle import *

setup(width = 1.0, height = 1.0)
title("Ghana Flag")
t = Turtle()
bgcolor("black")
t.speed(10)

SCALER = 15
########## CONSTANTS BASED ON TECHNICAL SPECIFICATIONS; DON'T MODIFY ###########
UNIT = 3
RED = "#CF0921"
YELLOW = "#FCD20F"
GREEN = "#006B3D"
D = 4.42
A = 0.21
VERTICES = 5
ANGLE = 360 / VERTICES
INT_ANGLE = 180 - 2 * ANGLE
################################################################################
def draw_rect(length, height, pen_colour=None, fill_colour=None, top_left=None):
    if top_left:
        t.pu()
        t.goto(top_left)
    if pen_colour:
        t.pencolor(pen_colour)
    if fill_colour:
        t.fillcolor(fill_colour)
        t.begin_fill()
    t.pd()
    for _ in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(height)
        t.rt(90)
    if fill_colour:
        t.end_fill()
    t.pu()

def draw_star(height, centre=None, pen_colour=None, fill_colour=None):
    t.pu()
    if centre:
        t.goto(centre)
    t.seth(90)
    t.fd(height / 2)
    t.seth(270)
    t.lt(INT_ANGLE / 2)
    t.pd()
    if pen_colour:
        t.pencolor(pen_colour)
    if fill_colour:
        t.fillcolor(fill_colour)
        t.begin_fill() 
    for _ in range(VERTICES):
        t.fd(height)
        t.rt(2 * ANGLE)
    if fill_colour:
        t.end_fill()
    t.pu()

draw_rect(18 * UNIT * SCALER, 4 * UNIT * SCALER, RED, RED, (-9 * UNIT * SCALER, 6 * UNIT * SCALER))
draw_rect(18 * UNIT * SCALER, 4 * UNIT * SCALER, YELLOW, YELLOW, (-9 * UNIT * SCALER, 2 * UNIT * SCALER))
draw_rect(18 * UNIT * SCALER, 4 * UNIT * SCALER, GREEN, GREEN, (-9 * UNIT * SCALER, -2 * UNIT * SCALER))
draw_star(4.2 * UNIT * SCALER , (0, -4), "black", "black")
t.ht()
done()

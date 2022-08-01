from turtle import *

def draw_circle(radius, pen_colour=None, fill_colour=None, start=None):
    if start:
        t.pu()
        t.goto(start)
    if pen_colour:
        t.pencolor(pen_colour)
    if fill_colour:
        t.fillcolor(fill_colour)
        t.begin_fill()
    t.pd()
    t.circle(radius)
    if fill_colour:
        t.end_fill()
    t.pu()

def draw_crescent(radius, offset, pen_colour=None, fill_colour=None, start=None):
    if start:
        t.pu()
        t.goto(start)
    draw_circle(radius, pen_colour, fill_colour)
    t.fd(offset)
    draw_circle(radius, bgcolor(), bgcolor())

if __name__ == "__main__":
    # setup(width = 1.0, height = 1.0)
    t = Turtle()
    bgcolor("black")
    t.speed(10)
    t.st()
    draw_crescent(50, 30, "white", "yellow", (-100, 200))
    done()
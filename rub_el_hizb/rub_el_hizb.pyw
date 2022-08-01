from turtle import *
import threading

L = 200
R = 40
t1, t2 = Turtle(), Turtle()
t1.hideturtle()
t2.hideturtle()
# t1.speed(6)
# t2.speed(6)
bgcolor("black")
t1.color("green")
t2.color("green")
# t2.color("yellow")
t1.pensize(5)
t2.pensize(5)

t1.pu()
t1.bk(L/2)
t1.lt(90)
t1.fd(L/2)
t1.rt(90)

t2.pu()
t2.lt(45)
t2.fd(L/2)
t2.rt(90)
t2.bk(L/2)

t1.pd()
t2.pd()
for i in range(4):
    t1.fd(L)
    t2.fd(L)
    t1.rt(90)
    t2.rt(90)
t1.pu()
t2.pu()
t1.home()
t1.rt(90)
t1.fd(R)
t1.lt(90)
t1.pd()
t1.circle(R)
done()

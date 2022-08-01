from turtle import *
from math import sqrt
import concurrent.futures
import threading

L = 60
SIDE = 2 * L + sqrt(2) * L
HALF_SIDE = SIDE / 2
R = 40
THICKNESS = 5
OFFSET = 3

# t1, t2, t3, t4 = Turtle(), Turtle(), Turtle(), Turtle()
turtles = [Turtle() for _ in range(4)]
# for t in turtles:
    # t.speed(10)

bgcolor("black")
for t in turtles:
    t.hideturtle()
    # t.speed(6)
    t.color("green")
    t.pensize(THICKNESS)
    t.pu()

turtles[0].goto(-HALF_SIDE, HALF_SIDE)
turtles[1].goto(HALF_SIDE, HALF_SIDE)
turtles[1].rt(90)
turtles[2].goto(-HALF_SIDE, -HALF_SIDE)
turtles[2].rt(270)
turtles[3].goto(HALF_SIDE, -HALF_SIDE)
turtles[3].rt(180)

for t in turtles:
    t.pd()

def draw_side(t):
    t.fd(L)
    t.lt(45)
    t.fd(L)
    t.rt(90)
    t.fd(L)
    t.lt(45)
    t.fd(L)
    t.rt(90)

# draw_side(turtles[0])
# draw_side(turtles[1])
# draw_side(turtles[3])
# draw_side(turtles[2])

# with concurrent.futures.ThreadPoolExecutor() as executor:
# # with concurrent.futures.ProcessPoolExecutor() as executor:
#     executor.map(draw_side, turtles)

# for t in turtles:
#     x = threading.Thread(target=draw_side, args=(t,))
#     x.start()

threads = [threading.Thread(target=draw_side, args=(t,)) for t in turtles]
for x in threads:
    x.start()


# for i in range(4):
#     draw_side(t1)
done()

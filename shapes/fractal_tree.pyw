from turtle import *

lt(90)

def draw(d):
	if d < 1:
		return
	else:
		fd(d)
		lt(30)
		draw(d/2)
		rt(60)
		draw(d/2)
		lt(30)
		bk(d)

draw(200)
done()
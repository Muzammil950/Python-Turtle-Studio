from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(72):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.01
    color(c)

    for j in range(6):
        fd(100)
        rt(60)

    rt(5)

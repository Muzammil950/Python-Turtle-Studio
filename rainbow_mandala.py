from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(120):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    color(c)
    circle(120)
    rt(3)

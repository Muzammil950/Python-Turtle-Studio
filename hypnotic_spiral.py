from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.002
    color(c)
    circle(i*0.5)
    lt(15)

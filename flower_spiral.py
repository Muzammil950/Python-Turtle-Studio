from turtle import *

speed(0)
bgcolor("black")
colors = ["red","yellow","orange","cyan","purple","green"]

for i in range(200):
    color(colors[i % 6])
    circle(i, 50)
    rt(91)

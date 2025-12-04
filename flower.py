from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(36):        # 36 petals (10° rotation each)
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)

    rt(10)        # rotate after each petal to complete the flower

done()

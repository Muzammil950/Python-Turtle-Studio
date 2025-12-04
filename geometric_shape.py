from turtle import *
import colorsys

speed(0)
bgcolor("black")

h = 0
for i in range(60):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.02
    color(c)

    for j in range(4):
        fd(120)
        rt(90)

    rt(6)

# Initial letter
penup()
goto(0, -10)
color("white")
write("M", align="center", font=("Arial", 40, "bold"))
hideturtle()
done()

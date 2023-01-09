import colorgram
from turtle import Screen
import turtle
import random
t = turtle.Turtle()
t.penup()
turtle.colormode(255)

colors = colorgram.extract('hirst.jpg', 20)
rgbcolors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b 
    newcolor = (r,g,b)
    rgbcolors.append(newcolor)

t.setheading(200)
t.forward(500)
t.setheading(0)

num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    t.dot(20,random.choice(rgbcolors))
    t.forward(50)
    
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


s = Screen()
s.exitonclick()

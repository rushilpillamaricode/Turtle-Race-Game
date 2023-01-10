from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=750,height=600) 

colors = ["red","orange","yellow","green","blue","purple"]
turtle_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for _ in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[_])
    t.turtlecolor = colors[_]
    t.penup()
    t.goto(x=-335,y=turtle_positions[_])
    turtles.append(t)

user = s.textinput(title="Make your bet",prompt="Choose your turtle: ")
cond = False
if user != "" and user in colors:
    cond = True

while cond:
    for turtle in turtles:
        if turtle.xcor() > 335:
            turtle.write("I won hurray!!!!")
            cond = False  
            break
        
        dist = random.randint(1,11)
        turtle.forward(dist)




s.exitonclick()

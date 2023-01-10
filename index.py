from turtle import Turtle,Screen
import keyboard

t = Turtle()
s = Screen()
t.speed("fastest")

def move_f():
    t.forward(10)

def move_b():
    t.backward(10)

def turn_l():
    t.setheading(t.heading() + 10)

def turn_r():
    t.setheading(t.heading() - 10)

def clear():
    t.speed("slowest")
    t.penup()
    t.home()
    t.pendown()
    t.speed("fastest")
    
def erase():
    t.clear()

s.listen()
s.onkeypress(key="Up",fun=move_f)
s.onkeypress(key="Left",fun=turn_l)
s.onkeypress(key="Right",fun=turn_r)
s.onkeypress(key="Down",fun=move_b)
s.onkeypress(key="space",fun=clear)
s.onkeypress(key="a",fun=erase)
s.exitonclick()from turtle import Turtle,Screen
import keyboard

t = Turtle()
s = Screen()
t.speed("fastest")

def move_f():
    t.forward(10)

def move_b():
    t.backward(10)

def turn_l():
    t.setheading(t.heading() + 10)

def turn_r():
    t.setheading(t.heading() - 10)

def clear():
    t.speed("slowest")
    t.penup()
    t.home()
    t.pendown()
    t.speed("fastest")
    
def erase():
    t.clear()

s.listen()
s.onkeypress(key="Up",fun=move_f)
s.onkeypress(key="Left",fun=turn_l)
s.onkeypress(key="Right",fun=turn_r)
s.onkeypress(key="Down",fun=move_b)
s.onkeypress(key="space",fun=clear)
s.onkeypress(key="a",fun=erase)
s.exitonclick()
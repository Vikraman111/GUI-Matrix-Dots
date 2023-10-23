import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t = (r, g, b)
    return t


t1 = Turtle()
t1.pensize(5)
t1.speed(10)
t1.shape("triangle")

start_x = -100
start_y = 100

for i in range(5):
    for j in range(5):
        t1.penup()
        t1.goto(start_x + j * 50, start_y - i * 50)
        t1.pendown()
        t1.dot(15)
        t1.penup()
        t1.color(random_color())


screen = Screen()
screen.exitonclick()

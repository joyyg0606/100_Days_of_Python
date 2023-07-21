from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()

timmy.pensize(5)

timmy.speed('fastest')
directions = [0, 90, 180, 270]
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(500):
    timmy.color(random_color())
    timmy.forward(15)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick() 
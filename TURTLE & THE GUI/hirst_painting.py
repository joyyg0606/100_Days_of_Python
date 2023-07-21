from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()
timmy.speed('fastest')
timmy.hideturtle()
turtle.colormode(255)
color_palette = [(249,128,128), (249,182,182), (195,146,146), (168,183,183), (136,210,210), (129,232,232), (181,229,229), (234,239,239), (220,214,214), (249,227,227), (255,205,205), (255,168,168)]

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_palette))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = Screen()
screen.exitonclick() 
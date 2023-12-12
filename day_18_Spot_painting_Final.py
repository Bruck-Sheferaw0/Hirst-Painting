from turtle import Turtle, Screen
import turtle
import random
colors_list=[(221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]
turtle.colormode(255)
dot = Turtle()
dot.penup()
dot.setheading(225)
dot.forward(350)
dot.setheading(0)
dot.speed(25)

num_dots = 101
for i in range(1,num_dots):
    dot.dot(20,random.choice(colors_list))
    dot.forward(50)
    if i % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)


screen = Screen()
screen.exitonclick()
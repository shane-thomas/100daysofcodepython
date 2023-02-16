import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
colors = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

tim.hideturtle()
tim.speed('fastest')
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
dots = 100

for dot in range(1, dots+1):
    tim.pendown()
    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)
    if dot%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


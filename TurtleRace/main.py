import turtle as t
from random import randint

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = t.Screen()
screen.setup(width = 500, height = 400)
bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle do you think will win the race? Enter the color: ")
ypos = [-100, -50, 0, 50, 100, 150]
turtles = []

for turtleno in range(0,6):
    new_turtle = t.Turtle(shape = 'turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtleno])
    new_turtle.goto(x = -230, y = ypos[turtleno])
    turtles.append(new_turtle)

if bet:
    race = True
while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You've won! the {winner} is the winner!")
            else:
                print(f"You lost. The winning turtle was {winner} in color.")
        step = randint(0,10)
        turtle.forward(step)
screen.exitonclick()

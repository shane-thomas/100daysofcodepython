import turtle as t

tim = t.Turtle()
screen = t.Screen()

def moveforward():
    tim.forward(10)

def movebackward():
    tim.backward(10)

def moveright():
    n = tim.heading() - 10 
    tim.setheading(n)

def moveleft():
    n = tim.heading() + 10
    tim.setheading(n)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=moveforward)
screen.onkey(key="a", fun=moveleft)
screen.onkey(key="d", fun=moveright)
screen.onkey(key="s", fun=movebackward)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

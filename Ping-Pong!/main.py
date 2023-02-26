from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=605)
screen.bgcolor("black")
screen.title("Ping-Pong!")

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(rpaddle.go_up, "Up")
screen.onkeypress(rpaddle.go_down,"Down")
screen.onkeypress(lpaddle.go_up, "w")
screen.onkeypress(lpaddle.go_down,"s")
scoreboard.update()

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ballreset()
        scoreboard.lpoint()
    
    if ball.xcor() < -380:
        ball.ballreset()
        scoreboard.rpoint()
        
screen.exitonclick()

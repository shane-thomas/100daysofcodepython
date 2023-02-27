import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    
    # Detecting if one of the cars hit the player and then end the game
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting if the player increased to a new level by reaching the end of the wall 
    if player.ycor() > 280:
        player.start()
        car_manager.levelup()
        scoreboard.increase()
        

screen.exitonclick()

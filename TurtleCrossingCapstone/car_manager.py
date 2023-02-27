from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            newcar = Turtle("square")
            newcar.shapesize(stretch_len=2, stretch_wid=1)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            randomy = random.randint(-250, 250)
            newcar.goto(300, randomy)
            self.all_cars.append(newcar)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def levelup(self):
        self.car_speed += MOVE_INCREMENT

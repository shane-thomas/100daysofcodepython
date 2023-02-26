from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "bold"))

    def lpoint(self):
        self.lscore+=1
        self.update()

    def rpoint(self):
        self.rscore+=1
        self.update()

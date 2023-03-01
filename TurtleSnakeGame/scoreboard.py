from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high.txt", "r") as file:
            self.high = int(file.read())
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high}", align="center", font=("Arial", 22, "normal"))
   
    def increase(self):
        self.score+=1
        self.clear()
        self.update()
    
    def reset(self):
        if self.score > self.high:
            self.high = self.score
            with open("high.txt","w") as file:
                file.write(str(self.score))
        self.score = 0

    # def over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

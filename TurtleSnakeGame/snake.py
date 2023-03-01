from turtle import Turtle
move = 20
startpos = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in startpos:
            self.add(position)
                
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            newx = self.segments[seg-1].xcor()
            newy = self.segments[seg-1].ycor()
            self.segments[seg].goto(newx,newy)
        self.head.forward(move)

    def add(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add(self.segments[-1].position())

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

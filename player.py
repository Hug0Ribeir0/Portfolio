from turtle import Turtle

MOVE = 20


class Player(Turtle):

    def __init__(self, px):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(px, 0)
        self.speed(9)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() -20
        self.goto(self.xcor(), y)

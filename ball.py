import random
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.touch = True  # True if player left touch
        self.starts = False
        self.speed(6)

    def move(self, pright, pleft):
        if self.starts:
            if self.ycor() >= 270:
                if self.touch:
                    self.setheading(random.randint(280, 340))
                else:
                    self.setheading(random.randint(200, 260))

            if self.ycor() <= -270:
                if not self.touch:
                    self.setheading(random.randint(100, 160))
                else:
                    self.setheading(random.randint(20, 80))

            if self.xcor() >= 435:
                self.forward(30)
                self.speed(0)
                self.goto(0, 0)
                self.starts = False
                return 1
            elif self.distance(pright) < 40 and self.xcor() > 0:
                self.touch = False
                self.setheading(random.randint(200, 300))

            if self.xcor() <= -435:
                self.forward(30)
                self.speed(0)
                self.goto(0, 0)
                self.starts = False
                return 2
            elif self.distance(pleft) < 40 and self.xcor() < 0:
                self.touch = True
                self.setheading(random.randint(20, 120))

            self.forward(20)

        return 0

    def start(self):
        self.setheading(random.randint(0, 360))
        self.speed(6)
        self.starts = True

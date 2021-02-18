from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.one = 0
        self.two = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.one}\t{self.two}", align=ALIGNMENT, font=FONT)

    def final(self):
        self.clear()
        self.goto(0,0)
        if self.one > self.two :
            self.write(f"WINNER - {self.one}", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"WINNER - {self.two}", align=ALIGNMENT, font=FONT)

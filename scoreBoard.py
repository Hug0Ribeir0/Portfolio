from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        #file = open("scores.txt") --> needs close manually
        with open("scores.txt", "r") as file:
            value = file.read()
            try:
                self.hscore = int(value)
            except:
                print("empty file")
        #close auto
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.hscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.hscore < self.score:
            self.hscore = self.score
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def end(self):
        with open("scores.txt", "w") as file:
            file.write(str(self.hscore))
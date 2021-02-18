import time

import player
from turtle import Screen, Turtle

from ball import Ball
from score import Score

S_WIDTH = 900
S_HEIGHT = 600

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)


# body = []
# t = Turtle("square")
# t.color("white")
# t.shape("square")
# t.goto(0,0)

b = Ball()
score = Score()

p_right = player.Player(px=420)
p_left = player.Player(px=(-420))
screen.listen()


screen.onkey(p_left.go_up, "w")
screen.onkey(p_left.go_down, "s")

screen.onkey(p_right.go_up, "Up")
screen.onkey(p_right.go_down, "Down")

screen.onkey(b.start, "p")

flag = True

while flag:
    screen.update()
    time.sleep(0.07)
    screen.update()
    result = b.move(p_right, p_left)
    if score.one == 3 or score.two == 3:
        break
    if result != 0:
        if result ==1:
            score.one = score.one +1
        else:
            score.two = score.two + 1
        score.update_scoreboard()


score.final()


screen.exitonclick()

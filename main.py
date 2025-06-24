from turtle import Turtle,Screen
from food import Food
from score import Score
import time
from snake import Snake
s=Screen()
f=Food()
score=Score()
s.title("my snake game")
s.bgcolor("black")
s.setup(600,600)
s.tracer(0)
sn=Snake()
s.listen()
s.onkey(sn.up, "Up")
s.onkey(sn.down, "Down")
s.onkey(sn.right, "Right")
s.onkey(sn.left, "Left")

game=True
while(game):
    s.update()
    time.sleep(0.1)

    sn.move()

    if sn.turtles[0].distance(f)<15:

        f.refresh()
        score.calculate()
        sn.extend(sn.turtles[-1].position())

    if sn.turtles[0].xcor()>290 or sn.turtles[0].xcor()<-290 or sn.turtles[0].ycor()>290 or sn.turtles[0].ycor()<-290:
        score.game()
        game=False
    for t in sn.turtles:
        if t==sn.turtles[0]:
            pass
        elif sn.turtles[0].distance(t)<15:
            score.game()
            game = False









s.exitonclick()


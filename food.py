from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        s=Screen()
        s.setup(600, 600)
        s.bgcolor("black")
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)



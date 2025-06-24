from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtles = []


        self.create()

    def create(self):
        x = 0
        y = 0

        for _ in range(3):
            i = Turtle("square")
            i.color("red")
            i.penup()
            i.goto(x, y)
            self.turtles.append(i)
            x -= 20
    def extend(self,position):
        for _ in range(3):
            i = Turtle("square")
            i.color("red")
            i.penup()
            i.goto(position)
            self.turtles.append(i)

    def move(self):
        for j in range(len(self.turtles) - 1, 0, -1):
            nx = self.turtles[j - 1].xcor()
            ny = self.turtles[j - 1].ycor()
            self.turtles[j].goto(nx, ny)
        self.turtles[0].forward(20)
    def up(self):
        if self.turtles[0].heading()!=270:
            self.turtles[0].setheading(90)




    def down(self):
        if self.turtles[0].heading()!=90:
            self.turtles[0].setheading(270)
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)


    def right(self):
        if self.turtles[0].heading() !=180:
            self.turtles[0].setheading(0)



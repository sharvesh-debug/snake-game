from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        s=Screen()
        self.color("white")



        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        s.setup(600,600)
        s.bgcolor("black")
        self.show()
        self.speed("fastest")


    def show(self):

        self.write(arg=f" current score: {self.score}",align="center",font=("Courier", 20, "bold"))
    def calculate(self):
        self.clear()
        self.score+=1
        self.show()
    def game(self):
        g=Turtle()
        g.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        g.write(arg="game over",align="center",font=("Courier", 20, "bold"))

from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(15)
        self.penup()
        self.goto(-200, 200)
        self.pendown()
        self.goto(200, 200)
        self.goto(200, -200)
        self.goto(-200, -200)
        self.goto(-200, 200)
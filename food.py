from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.random_position()

    def random_position(self):
        rand_x_coor = random.randint(-180, 180)
        rand_y_coor = random.randint(-180, 180)
        self.goto(rand_x_coor, rand_y_coor)
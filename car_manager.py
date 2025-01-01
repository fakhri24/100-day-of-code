from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.speed_move = STARTING_MOVE_DISTANCE
        self.all_car = []
        self.create_car()
        self.delete_vanish_car()
        # Screen().ontimer(CarManager, 200)

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        rand_color = random.choice(COLORS)
        new_car.color(rand_color)
        rand_y = random.randint(-250, 250)
        new_car.goto(320, rand_y)
        self.all_car.append(new_car)

    def move(self):
        for _ in range(len(self.all_car)):
            self.all_car[_].forward(self.speed_move)

    def increase_speed_move(self):
        self.speed_move += MOVE_INCREMENT

    def delete_vanish_car(self):
        for _ in range(len(self.all_car)):
            if self.all_car[_].xcor() < 320:
                self.all_car.remove(self.all_car[_])

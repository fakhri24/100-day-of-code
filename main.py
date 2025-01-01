import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # screen.ontimer(car.create_car(), 1000)
    car.move()
    i += 1
    if i == 3:
        car.create_car()
    elif i > 3:
        i = 0

    if player.ycor() > 280:
        player.restart()
        car.increase_speed_move()
        scoreboard.increase()

    num_car = len(car.all_car)
    for _ in range(num_car):
        if (player.distance(car.all_car[_]) < 30 and
                car.all_car[_].ycor() - 20 < player.ycor() < car.all_car[_].ycor() + 20):
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

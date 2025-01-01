from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Eat Not Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
wall = Wall()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # karena ular bergerak dengan kecepatan 20, maka ada kemungkinan jarak antara pusat kepala ular
    # dan pusat food lebih dari 15, padahal dalam grafiknya badan ular itu menyentuh food
    # mungkin bisa diperbaiki dengan mengubah jaraknya menjadi 10 (?)
    # Ternyata tidak bisa, malah membuat ularnya makin pendek
    # oke, simpan dulu masalah ini buat nanti
    if food.distance(snake.head.xcor(), snake.head.ycor()) < 15:
        food.random_position()
        snake.extend_body()
        scoreboard.keep_score()

    if snake.head.xcor() > 190 or snake.head.xcor() < -190 or snake.head.ycor() > 190 or snake.head.ycor() < -190:
        game_is_on = False
        scoreboard.game_over()

    for scan in snake.full_snake[1:]:
        if snake.head.distance(scan) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

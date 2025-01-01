from turtle import Turtle

STARTING_POSITION = [(0, 0), (-15, 0), (-30, 0)]
MOVE_DISTANCE = 15
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.full_snake = []
        self.snake_body()
        self.head = self.full_snake[0]

    def snake_body(self):
        for position in STARTING_POSITION:
            self.new_body_part(position)

    def new_body_part(self, position):
        part_snake = Turtle()
        part_snake.shape("square")
        part_snake.shapesize(0.75, 0.75)
        part_snake.color("white")
        part_snake.penup()
        # ini gagal dalam menyimpan koordinat posisi ekor ular
        # part_snake.goto(-20 * move_var, 0)
        part_snake.goto(position)
        self.full_snake.append(part_snake)

    def extend_body(self):
        self.new_body_part(self.full_snake[-1].position())

    def move(self):
        for part_n in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[part_n - 1].xcor()
            new_y = self.full_snake[part_n - 1].ycor()
            self.full_snake[part_n].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

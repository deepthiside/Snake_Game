from turtle import Turtle, Screen
import random
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake setup
snake = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(pos)
    snake.append(segment)

# Food setup
food = Turtle("circle")
food.color("red")
food.shapesize(0.5, 0.5)
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Direction setup
direction = "stop"
has_moved = False  # ← This will track whether movement has started

# Movement functions
def go_up():
    global direction, has_moved
    if direction != "down":
        direction = "up"
        has_moved = True

def go_down():
    global direction, has_moved
    if direction != "up":
        direction = "down"
        has_moved = True

def go_left():
    global direction, has_moved
    if direction != "right":
        direction = "left"
        has_moved = True

def go_right():
    global direction, has_moved
    if direction != "left":
        direction = "right"
        has_moved = True

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Move function
def move():
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)

    if direction == "up":
        snake[0].setheading(90)
        snake[0].forward(20)
    elif direction == "down":
        snake[0].setheading(270)
        snake[0].forward(20)
    elif direction == "left":
        snake[0].setheading(180)
        snake[0].forward(20)
    elif direction == "right":
        snake[0].setheading(0)
        snake[0].forward(20)

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    move()

    if has_moved:
        # Collision with food
        if snake[0].distance(food) < 15:
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            snake.append(new_segment)

        # Collision with self
        for segment in snake[1:]:
            if segment.distance(snake[0]) < 10:
                game_on = False
                game_over = Turtle()
                game_over.hideturtle()
                game_over.color("red")
                game_over.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

screen.mainloop()

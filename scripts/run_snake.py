#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
import time
import turtle
from random import randint


def configure_screen():
    """Configure the Game Screen"""
    screen = turtle.Screen()
    screen.title("The Snake Game")
    screen.bgcolor("yellow")
    screen.setup(640, 480)
    # Turns turtle animation on/off and set delay for update drawings.
    screen.tracer(0)
    return screen


def main():
    screen = configure_screen()

    # the points
    points = 0
    scoreboard = turtle.Turtle()
    scoreboard.speed(0)
    scoreboard.color("blue")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, screen.window_height() // 2 - 40)
    scoreboard.write(
        f"Points: {points}", align="center", font=("Courier", 24, "normal")
    )

    # the snake head
    head = turtle.Turtle()
    head.fillcolor("black")
    head.shape("turtle")
    head.penup()
    head.goto(0, 0)

    # the snake body
    snake = [head]

    def add_segment():
        segment = turtle.Turtle()
        segment.penup()
        segment.goto(head.xcor(), head.ycor())
        segment.setheading(head.heading())
        segment.shape("turtle")
        segment.fillcolor("green")
        segment.speed(0)
        snake.append(segment)

    # the food
    food = turtle.Turtle()
    food.shape("circle")
    food.fillcolor("red")
    food.penup()

    def move_food():
        x_limit = screen.window_width() // 2 - 10
        y_limit = screen.window_height() // 2 - 10
        food.goto(randint(-x_limit, x_limit), randint(-y_limit, y_limit))

    def move():
        """Move the the Snake"""
        for i in range(len(snake) - 1, 0, -1):
            snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())
            snake[i].setheading(snake[i - 1].heading())

        if head.heading() == 0:
            head.setx(head.xcor() + 24)
        elif head.heading() == 90:
            head.sety(head.ycor() + 24)
        elif head.heading() == 180:
            head.setx(head.xcor() - 24)
        elif head.heading() == 270:
            head.sety(head.ycor() - 24)
        else:
            raise ValueError(
                f"Snake can only move vertically or horizontally: {head.heading()}"
            )

    def go_up():
        if head.heading() != 270:
            head.setheading(90)

    def go_down():
        if head.heading() != 90:
            head.setheading(270)

    def go_right():
        if head.heading() != 180:
            head.setheading(0)

    def go_left():
        if head.heading() != 0:
            head.setheading(180)

    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.listen()

    def check_collision():
        if (
            abs(head.xcor()) >= screen.window_width() // 2 - 10
            or abs(head.ycor()) >= screen.window_height() // 2 - 10
        ):
            return True

        for s in snake[1:]:
            if head.distance(s) <= 20:
                return True

        return False

    def check_food():
        return head.distance(food) <= 18

    # move the food
    move_food()

    # the sleep time (in seconds)
    sleep = 0.25

    while True:
        # refresh the screen
        screen.update()

        # move the snake
        move()

        if check_collision():
            time.sleep(1)
            head.goto(0, 0)
            head.setheading(0)
            sleep = 0.25
            points = 0
            move_food()
            for s in snake[1:]:
                s.reset()
                s.hideturtle()
            snake = [head]
            scoreboard.clear()
            scoreboard.write(
                f"Points: {points}", align="center", font=("Courier", 24, "normal")
            )

        if check_food():
            move_food()
            sleep = max(0.05, sleep - 0.01)
            add_segment()
            points += 1
            scoreboard.clear()
            scoreboard.write(
                f"Points: {points}", align="center", font=("Courier", 24, "normal")
            )

        # sleep
        time.sleep(sleep)


if __name__ == "__main__":
    main()

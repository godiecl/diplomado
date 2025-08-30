#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada

import turtle
from random import randint


def configure_screen():
    screen = turtle.Screen()
    screen.title("The Random Turtle")
    screen.setup(640, 480)
    return screen


def main():
    screen = configure_screen()
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor("red")
    t.penup()

    x_limit = screen.window_width() // 2 - 10
    y_limit = screen.window_height() // 2 - 10

    def move_and_dot():
        x = randint(-x_limit, x_limit)
        y = randint(-y_limit, y_limit)
        t.goto(x, y)
        t.dot(10)
        screen.ontimer(move_and_dot, 250)

    move_and_dot()

    screen.exitonclick()


if __name__ == "__main__":
    main()

#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
import turtle


def configure_screen():
    screen = turtle.Screen()
    screen.title("The Base Turtle")
    screen.setup(640, 480)
    return screen


def main():
    screen = configure_screen()

    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor("red")

    for i in range(4):
        t.forward(100)
        t.left(90)

    for i in range(50, 100, 50):
        for j in range(3):
            t.dot(20)
            t.forward(i)
            t.left(120)

    screen.exitonclick()


if __name__ == "__main__":
    main()

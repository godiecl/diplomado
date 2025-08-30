#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
import turtle
from math import cos, pi, sin, atan2, degrees


def configure_screen():
    screen = turtle.Screen()
    screen.title("The Flighting Dot")
    screen.setup(640, 480)
    screen.setworldcoordinates(0, 0, 500, 500)
    return screen


def main():
    screen = configure_screen()
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor("red")

    angle = 75
    gravity = 9.81
    speed_kmh = 350

    speed_mts = speed_kmh * 1000 / 3600
    angle_rad = angle * pi / 180
    v_x = speed_mts * cos(angle_rad)
    v_y = speed_mts * sin(angle_rad)
    flight_time = 2 * v_y / gravity

    steps = 100
    interval_time = flight_time / steps

    for step in range(steps + 1):
        t_time = step * interval_time
        x = v_x * t_time
        y = v_y * t_time - (0.5 * gravity * t_time**2)
        ar = atan2(v_y - gravity * t_time, v_x)
        t.setheading(degrees(ar))
        t.goto(x, y)
        t.dot(5)

    turtle.done()


if __name__ == "__main__":
    main()

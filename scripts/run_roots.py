#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
import cmath
from math import sqrt


def cuadratic_root(a: int, b: int, c: int):
    """Function to calculate the roots"""
    if a == 0:
        raise ValueError("a cannot be zero")

    disc = b**2 - 4 * a * c
    if disc >= 0:
        root_1 = (-b + sqrt(disc)) / (2 * a)
        root_2 = (-b - sqrt(disc)) / (2 * a)
    else:
        root_1 = (-b + cmath.sqrt(disc)) / (2 * a)
        root_2 = (-b - cmath.sqrt(disc)) / (2 * a)

    return root_1, root_2


def main():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = int(input("Enter value of c:"))

    print(f"Valor de a, b y c: {a}, {b} y {c}.")

    root_1, root_2 = cuadratic_root(a, b, c)
    print(f"Root 1: {root_1}.")
    print(f"Root 2: {root_2}.")


if __name__ == "__main__":
    main()

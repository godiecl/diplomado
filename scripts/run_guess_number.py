#  Copyright (c) 2025. Diplomado en Inteligencia Artificial Aplicada
from random import randint


def main():
    max_number = 500
    secret_number = randint(1, max_number)
    guess_number = 0

    while True:
        user_guess = int(input(f"Guess the number (1->{max_number}): "))
        guess_number += 1

        if user_guess < secret_number:
            print("Too low!")
        elif user_guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations !!")
            print(f"You've guessed the number {secret_number} ..")
            print(f".. in {guess_number}.")
            break


if __name__ == "__main__":
    main()

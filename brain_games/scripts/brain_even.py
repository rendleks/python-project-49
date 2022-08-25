#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    correct_answer = 0

    while True:
        generate_numbers = randint(1, 100)


        print("Question:", generate_numbers)
        answer = prompt.string("Your answer: ")

        if generate_numbers % 2 == 0 and answer == 'yes':
            correct_answer += 1
            print("Correct!")
        elif generate_numbers % 2 != 0 and answer == 'no':
            correct_answer += 1
            print("Correct!")
        elif generate_numbers % 2 != 0 and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!")
            correct_answer = 0
        elif generate_numbers % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!")
            correct_answer = 0

        if correct_answer == 3:
            print(f"Congratulations, {name}!")
            break


def main():
    welcome_user()


if __name__ == "__main__":
    main()

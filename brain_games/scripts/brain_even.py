#!/usr/bin/env python3
import prompt
from random import randint


ANSWER_YES = 'yes'
ANSWER_NO = 'no'


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

        if generate_numbers % 2 == 0 and answer == ANSWER_YES:
            correct_answer += 1
            print("Correct!")
        elif generate_numbers % 2 != 0 and answer == ANSWER_NO:
            correct_answer += 1
            print("Correct!")
        elif generate_numbers % 2 != 0 and answer == ANSWER_YES:
            print(f"'{ANSWER_YES}' is wrong answer ;(. "
                  "Correct answer was '{ANSWER_NO}'."
                  "\nLet's try again, {name}!")
            break
        elif generate_numbers % 2 == 0 and answer == ANSWER_NO:
            print(f"'{ANSWER_NO}' is wrong answer ;(. "
                  "Correct answer was '{ANSWER_YES}'."
                  "\nLet's try again, {name}!")
            break

        if correct_answer == 3:
            print(f"Congratulations, {name}!")
            break


def main():
    welcome_user()


if __name__ == "__main__":
    main()

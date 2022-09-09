#!/usr/bin/env python3
import prompt
from random import randint, choice


def welcome_user():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("What is the result of the expression?")

    right_answer = 0

    while True:

        random_num1 = randint(1, 30)
        random_num2 = randint(1, 30)
        random_choice = choice(["+", "-", "*"])

        print(f"Question: {random_num1} {random_choice} {random_num2}")
        answer = int(input("Your answer: "))
        correct_answer = int(eval(f"{random_num1}\
                                  {random_choice} {random_num2}"))

        if answer == correct_answer:
            print("Correct!")
            right_answer += 1
        else:
            print(f"\'{answer}\' is wrong answer ;(."
                  "Correct answer was \'{correct_answer}\'.")
            print(f"Let's try again, {name}!")
            break

        if right_answer == 3:
            print(f"Congratulations, {name}!")
            break


def main():
    welcome_user()


if __name__ == "__main__":
    main()

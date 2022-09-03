#!/usr/bin/env python3
import prompt
from random import randint, choice

def progression():

    num_progression = randint(3, 19)
    start_progression = randint(1, 100)
    finish_progression = start_progression * 10

    nums_progression = [i for i in range(start_progression, finish_progression, num_progression)]

    print(num_progression)


def welcome_user():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("Find the greatest common divisor of given numbers.")

    right_answer = 0

    while True:

        random_num1 = randint(1, 30)
        random_num2 = randint(1, 30)


        print(f"Question: {random_num1} {random_num2}")
        answer = int(input("Your answer: "))
        correct_answer = nok(random_num1, random_num2)

        if answer == correct_answer:
            print("Correct!")
            right_answer += 1
        else:
            print(f"\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.")
            print(f"Let's try again, {name}!")
            right_answer = 0

        if right_answer == 3:
            print(f"Congratulations, {name}!")
            break

def main():
    progression()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_even import ANSWER_NO, ANSWER_YES


def random_simple_num():

    random_number = randint(1, 1000)

    k = 0

    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            k = k + 1

    if k == 0:
        return random_number, True
    return random_number, False


def game_prime():

    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}")
    print("Answer \"yes\" if given number is prime. "
          "Otherwise answer \"no\".")

    count_correct_answer = 0

    while True:

        random_num, is_prime = random_simple_num()

        print("Question:", random_num)

        you_answer = input("Your answer: ")

        if you_answer == ANSWER_YES and is_prime:
            print('Correct!')
            count_correct_answer += 1
        elif you_answer == ANSWER_NO and not is_prime:
            print('Correct!')
            count_correct_answer += 1
        elif you_answer == ANSWER_NO and is_prime or \
                you_answer == ANSWER_YES and not is_prime:
            print(f"'{ANSWER_NO}' is wrong answer ;(."
                  f"Correct answer was '{ANSWER_YES}'.")
            print(f"Let's try again, {user_name}!")
            break
        if count_correct_answer == 3:
            print(f"Congratulations, {user_name}!")
            break


def main():
    game_prime()


if __name__ == "__main__":
    main()

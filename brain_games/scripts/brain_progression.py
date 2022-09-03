#!/usr/bin/env python3
from random import randint

def progression():

    num_progression = randint(3, 15)
    start_progression = randint(1, 100)
    
    finish_progression = start_progression + (num_progression * 10)
    removed_num_in_progression = randint(1, 9) # случайное число, будет заменено на две точки ..
    
    progression_sequence = [str(i) for i in range(start_progression, finish_progression, num_progression)] # создание верной последовательности

    correct_result = progression_sequence[removed_num_in_progression]

    progression_sequence[removed_num_in_progression] = ".."

    return progression_sequence, int(correct_result)


def game_progression():

    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}")
    print("What number is missing in the progression?")

    count_correct_answer = 0

    while True:

        progression_nums, correct_answer = progression()

        print("Question:", " ".join(progression_nums))

        you_answer = int(input("Your answer: "))

        if you_answer == correct_answer:
            print('Correct!')
            count_correct_answer += 1
        else:
            print(f"'{you_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            count_correct_answer = 0

        if count_correct_answer == 3:
            print(f"Congratulations, {user_name}!")
            
                        
game_progression()
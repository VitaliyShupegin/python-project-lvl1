#!/usr/bin/env python3
import prompt
from random import randint


def is_even():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    index = 0
    count = 3
    Congratulations = print('Congratulations, {name}!')
    while index < count:
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            index += 1
        elif random_number % 2 != 0 and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            index += 1
        elif random_number % 2 == 0 and answer == 'no':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            index += 1
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            index += 1
    return Congratulations

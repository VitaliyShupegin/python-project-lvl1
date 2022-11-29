#!/usr/bin/env python3
import prompt

ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}')
    print(game.TASK)
    index = 0

    while index < ROUNDS:
        question, correct_answer = game.question_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct !')
            index += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {name}!"
            )
            return
    print(f'Congratulations, {name}!')

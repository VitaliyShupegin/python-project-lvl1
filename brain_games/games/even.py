#!/usr/bin/env python3
from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_question_and_answer():
    question = randint(0, 100)
    correct_answer = is_even(question)
    return str(question), correct_answer

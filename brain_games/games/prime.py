#!/usr/bin/env python3
from random import randint
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    while i < num:
        if num % i != 0:
            i += 1
        else:
            return False
    return True


def get_question_and_answer():
    question = randint(0, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer

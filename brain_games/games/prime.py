#!/usr/bin/env python3
from random import randint
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(num):
    result = 2
    while num % result != 0:
        result += 1
    return result == num


def question_answer():
    question = randint(0, 100)
    if is_prime(question):
          correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

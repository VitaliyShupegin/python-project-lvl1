#!/usr/bin/env python3
from random import randint, choice
TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    num1 = randint(0, 10)
    step = randint(1, 10)
    result = []
    for i in range(10):
        next_step = num1 + step * i
        result.append(str(next_step))
    elem = choice(range(len(result) - 1))
    correct_answer = result[elem]
    result[elem] = '..'
    question = " ".join(result)
    return question, correct_answer

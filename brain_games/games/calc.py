#!/usr/bin/env python3
from random import randint, choice

TASK = 'What is the result of the expression?'


def question_answer():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    oper = choice(['+', '-', '*'])
    question = f'{num1} {oper} {num2}'

    if oper == '+':
        correct_answer = num1 + num2
    elif oper == '-':
        correct_answer = num1 - num2
    elif oper == '*':
        correct_answer = num1 * num2
    return question, correct_answer

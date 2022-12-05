#!/usr/bin/env python3
from random import randint, choice

TASK = 'What is the result of the expression?'


def question_answer():
    num1 = randint(0, 20)
    num2 = randint(0, 20)
    oper = choice(['+', '-', '*'])
    question = f'{str(num1)} {oper} {str(num2)}'

    if oper == '+':
        correct_answer = num1 + num2
    elif oper == '-':
        correct_answer = num1 - num2
    elif oper == '*':
        correct_answer = num1 * num2
    return question, str(correct_answer)

#!/usr/bin/env python3
from random import randint
from random import choice

TASK = 'What is the result of the expression?'

def question_answer():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    oper = choice(['+', '-', '*'])
    question = f'Question: {num1} {oper} {num2}'

    if oper == '+':
        correct_answer = (num1 + num2)
    elif oper == '-':
        correct_answer = (num1 - num2)
    elif oper == '*':
        correct_answer = (num1 * num2)
    return question, correct_answer

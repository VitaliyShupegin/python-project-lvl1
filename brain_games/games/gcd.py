#!/usr/bin/env python3
from random import randint
import math
TASK = 'Find the greatest common divisor of given numbers.'

def question_answer():
    num1 = randint(0, 20)
    num2 = randint(0, 20)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
from random import randint, choice

TASK = 'What is the result of the expression?'


def get_arithmetic_expression(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    return result


def get_question_and_answer():
    num1 = randint(0, 20)
    num2 = randint(0, 20)
    operator = choice(['+', '-', '*'])
    question = f'{num1} {operator} {num2}'
    correct_answer = str(get_arithmetic_expression(num1, num2, operator))
    return question, correct_answer

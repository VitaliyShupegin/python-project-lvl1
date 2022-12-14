from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return False

        i += 1
    return True


def get_question_and_answer():
    question = randint(0, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer

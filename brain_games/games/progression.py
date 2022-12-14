from random import randint

TASK = 'What number is missing in the progression?'


def generate_progression(start, stop, interval):

    list = [str(i) for i in range(start, stop, interval)]

    return list


def get_question_and_answer():
    interval = randint(1, 10)
    start = randint(1, 10)
    stop = start + (interval * 10)
    progression = generate_progression(start, stop, interval)
    index_replace = randint(0, len(progression) - 1)
    correct_answer = progression[index_replace]
    progression[index_replace] = '..'
    question = " ".join(progression)
    return question, correct_answer

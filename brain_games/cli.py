import prompt

def welcome_user():
    name = prompt.string('May I have your name?')
    name = prompt.string('Hello ,' + name + '!')
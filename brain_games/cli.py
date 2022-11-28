import prompt

def welcome_user():
    name = prompt.string('May I have name?')
    name = prompt.string('Hello, ' + name + '!')
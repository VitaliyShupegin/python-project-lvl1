#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have name?')
    print(f'Hello, {name}!')

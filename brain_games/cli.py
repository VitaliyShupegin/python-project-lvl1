#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have name?')
    name = prompt.string(f'Hello, {name}!')

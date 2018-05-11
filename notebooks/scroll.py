from time import sleep
import sys
import random

version = "v0.1"


def run(scene):
    if scene == "temple":
        run_temple()

def run_temple()
    text = "Welcome adept are you ready to begin your training?"
    type_text(text)
    force_answer('y')
    type_text(


def force_answer(wanted, prompt='$'):
    try_again = ['Are you sure?',
                 'Please input another answer',
                 'Did you try %s' % wanted,
                 'I say my leige perhaps you should pick another answer',
                 prompt
                 ]

    user_input = ''
    wanted = wanted.lower()
    while user_input != wanted:
        user_input = input(prompt).lower()
        if user_input != wanted:
            prompt = random.choice(try_again)


def type_text(text):
    for idx, word in enumerate(text.split()):
        if idx > 0:
            sys.stdout.write(' ')
        val = random.randint(0, 1)
        if val:
            type_word(word)
        else:
            sys.stdout.write(word)
            sys.stdout.flush()


def type_word(word):
    for char in word:
        sleep(random.uniform(0.1, 0.3))
        sys.stdout.write(char)
        sys.stdout.flush()

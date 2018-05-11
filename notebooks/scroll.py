from time import sleep
import sys
import random

version = "v0.1"


def run(scene):
    if scene == "temple":
        run_temple()


def run_temple():
    text = "Welcome adept are you ready to begin your training?"
    type_text(text)
    force_answer('y')
    type_text("Ah, good choice... let's begin then.")
    type_text("As telepaths, we connect mind, device, and code, routing messages from one place to"
              " another on behalf of the guild. This is especially beneficiary when wizards want"
              " to craft spells to talk to enchanted objects, or enchantresses want wizard spells"
              " to enhance their enchanted items."
              )
    type_text("This difficult task requires concentration and organization.  We enhance these"
              " attributes in ourselves as we train in silence…"
              )
    type_text("Adept you must empty your mind to receive the teachings.")
    type_text("Is your mind clear? Are you ready to continue? ")
    force_answer('y')
    type_text("Excellent! Complete the exercise below, and I'll come back to check your work")
    type_text("Shutting down interface.....")


def force_answer(wanted, prompt='$'):
    try_again = ['Are you sure?',
                 'Please input another answer',
                 'Did you try %s' % wanted,
                 'I say my leige perhaps you should pick another answer',
                 prompt
                 ]

    user_input = ''
    wanted = wanted.lower()
    len_wanted = len(wanted)
    while user_input[:len_wanted] != wanted:
        user_input = input(prompt).lower()
        if user_input[:len_wanted] != wanted:
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
    print("\n")


def type_word(word):
    for char in word:
        sleep(random.uniform(0.1, 0.3))
        sys.stdout.write(char)
        sys.stdout.flush()

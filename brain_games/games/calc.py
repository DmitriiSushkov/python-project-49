from operator import add, sub, mul
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}


def generate_round():
    num_one, num_two = randint(1, 25), randint(1, 25)
    sign = choice(list(OPERATORS.keys()))
    if num_one > num_two:
        question = f'{num_one} {sign} {num_two}'
    elif num_two > num_one:
        question = f'{num_two} {sign} {num_one}'
    correct_answer = str(abs(OPERATORS[sign](num_one, num_two)))
    return question, str(correct_answer)

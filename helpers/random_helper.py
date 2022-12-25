import random
import string
from typing import Final


def get_random_numbers(length=10):
    return ''.join(random.choices(string.digits, k=length))


def get_random_name(length):
    return ''.join(random.choices(string.ascii_letters, k=length))


def get_random_email(prefix='mail', domain='mx.com'):
    """we hypothesize that with the (2*26)^8 is a pretty huge number of combinations to not get any collisions"""
    # TODO later we need to have a stored counter and simplify this by just incrementing
    return f'{prefix}{get_random_name(8)}@{domain}'


if __name__ == '__main__':
    print('random name', get_random_name(5))
    print('random digits', get_random_numbers())
    print('random email', get_random_email())

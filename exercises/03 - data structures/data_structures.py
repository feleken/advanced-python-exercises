def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s1 = 'lol'
s2 = 'abc'
print('{} is a palindrome? {}'.format(s1, is_palindrome(s1)))
print('{} is a palindrome? {}'.format(s2, is_palindrome(s2)))

def invert(dict_original):
    dict_inverse = {v: k for k, v in dict_original.items()}
    return dict_inverse

dict_a = {'a': 1, 'b': 2}
print('The dict {} is reversed like this: {}'.format(dict_a, invert(dict_a)))

import random

def spongecase(s):
    spongecase_string = ''
    for id, char in enumerate(s):
        if id % 2 == 0:
            spongecase_string += char
        else:
            spongecase_string += char.upper()

    return spongecase_string

s3 = 'spongebob'
print(spongecase(s3))

def spongecase_random(s):
    spongecase_string = ''
    for id, char in enumerate(s):
        if random.randint(1,100) <= len(s):
            spongecase_string += char.upper()
        else:
            spongecase_string += char

    return spongecase_string

s4 = 'spongebob sentence is random'
print(spongecase_random(s4))

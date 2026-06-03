import sys

INITIAL = 'INITIAL'
FOUND_0 = 'FOUND_0'
FOUND_X = 'FOUND_X'
FOUND_NUMBER = 'FOUND_NUMBER'

for line in sys.stdin:
    state = INITIAL
    token = ''
    for character in line:
        if state == INITIAL and character == '0':
            token += character
            state = FOUND_0
        elif state == FOUND_0 and (character.lower() == 'x'):
            token += character
            state = FOUND_X
        elif state in [FOUND_X, FOUND_NUMBER] and (character.isnumeric() or character.lower() in ['a', 'b', 'c', 'd', 'e', 'f']):
            token += character
            state = FOUND_NUMBER
        elif state == FOUND_NUMBER:
            decimal = int(token, 16)
            print(token, decimal)
            token = ''
            state = INITIAL
        else:
            token = ''
            state = INITIAL

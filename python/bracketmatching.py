def checkSequence(sequence):
    unclosedBrackets = []
    for character in sequence:
        if character == '(':
            unclosedBrackets.append(')')
        elif character == '[':
            unclosedBrackets.append(']')
        elif character == '{':
            unclosedBrackets.append('}')
        elif len(unclosedBrackets) != 0:
            unclosedBracket = unclosedBrackets.pop()
            if character != unclosedBracket:
                return False
        else:
            return False

    return 0 == len(unclosedBrackets)


_ = input()
sequence = input()
isValid = checkSequence(sequence)
if isValid:
    print('Valid')
else:
    print('Invalid')

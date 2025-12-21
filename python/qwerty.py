def mapKey(key):
    match key:
        case 'a': return 'q'
        case 'b': return 'w'
        case 'c': return 'e'
        case 'd': return 'r'
        case 'e': return 't'
        case 'f': return 'y'
        case 'g': return 'u'
        case 'h': return 'i'
        case 'i': return 'o'
        case 'j': return 'p'
        case 'k': return 'a'
        case 'l': return 's'
        case 'm': return 'd'
        case 'n': return 'f'
        case 'o': return 'g'
        case 'p': return 'h'
        case 'q': return 'j'
        case 'r': return 'k'
        case 's': return 'l'
        case 't': return 'z'
        case 'u': return 'x'
        case 'v': return 'c'
        case 'w': return 'v'
        case 'x': return 'b'
        case 'y': return 'n'
        case 'z': return 'm'
        case ' ': return ' '

_ = input()
text = input()
result = ''
for letter in text:
    result += mapKey(letter)

print(result)

def alphabetMapping(character):
    return {
        "a": "@",
        "b": "8",
        "c": "(",
        "d": "|)",
        "e": "3",
        "f": "#",
        "g": "6",
        "h": "[-]",
        "i": "|",
        "j": "_|",
        "k": "|<",
        "l": "1",
        "m": "[]\/[]",
        "n": "[]\[]",
        "o": "0",
        "p": "|D",
        "q": "(,)",
        "r": "|Z",
        "s": "$",
        "t": "']['",
        "u": "|_|",
        "v": "\/",
        "w": "\/\/",
        "x": "}{",
        "y": "`/",
        "z": "2",
    }.get(character, character)


text = list(input().lower())
output = ""
for character in text:
    output += alphabetMapping(character)

print(output)

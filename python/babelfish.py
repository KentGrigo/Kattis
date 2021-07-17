dictionary = {}
while True:
    entry = input()
    if entry == "":
        break

    english, babelfish = entry.split()
    dictionary[babelfish] = english

while True:
    try:
        message = input()
    except EOFError:
        break

    translation = dictionary.get(message, "eh")
    print(translation)

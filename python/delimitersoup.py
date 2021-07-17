def syntaxCheck(program):
    stack = []
    for index, character in enumerate(program):
        if character in ["(", "[", "{"]:
            stack.append(character)
        elif character in [")", "]", "}"]:
            try:
                lastOpeningDelimter = stack.pop()
            except IndexError:
                return (character, index)

            if lastOpeningDelimter == "(" and character != ")" or \
                lastOpeningDelimter == "[" and character != "]" or \
                lastOpeningDelimter == "{" and character != "}":
                    return (character, index)

    return None


_ = input()
program = list(input())
error = syntaxCheck(program)
if error == None:
    print("ok so far")
else:
    character, index = error
    print("{} {}".format(character, index))

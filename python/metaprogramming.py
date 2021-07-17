def define(command, state):
    value = int(command[1])
    variable = command[2]
    state[variable] = value

def evaluate(command, state):
    operand = command[2]
    variable1 = command[1]
    variable2 = command[3]

    if variable1 not in state or variable2 not in state:
        print("undefined")
        return

    value1 = state[variable1]
    value2 = state[variable2]

    if operand == "=":
        result = value1 == value2
    elif operand == "<":
        result = value1 < value2
    elif operand == ">":
        result = value1 > value2
    else:
        raise AttributeError

    if result:
        print("true")
    else:
        print("false")


state = {}
while True:
    try:
        command = input().split()
    except EOFError:
        break

    instruction = command[0]
    if instruction == "define":
        define(command, state)
    elif instruction == "eval":
        evaluate(command, state)
    else:
        raise AttributeError

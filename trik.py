actions = input()

def actionA(x):
    return {
        1: 2,
        2: 1,
        3: 3,
    }[x]

def actionB(x):
    return {
        1: 1,
        2: 3,
        3: 2,
    }[x]

def actionC(x):
    return {
        1: 3,
        2: 2,
        3: 1,
    }[x]

placement = 1
for action in actions:
    if action == "A":
        placement = actionA(placement)
    elif action == "B":
        placement = actionB(placement)
    else:
        placement = actionC(placement)

print(placement)
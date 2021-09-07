lengthOfLog = int(input())
state = {}
for _ in range(lengthOfLog):
    action, name = input().split()
    isInside = state.get(name, False)
    if action == "entry":
        state[name] = True
        if isInside:
            output = "{} entered (ANOMALY)"
        else:
            output = "{} entered"
    else:
        state[name] = False
        if isInside:
            output = "{} exited"
        else:
            output = "{} exited (ANOMALY)"

    print(output.format(name))

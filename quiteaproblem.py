while True:
    try:
        line = input()
    except EOFError:
        break

    if "problem" in line.lower():
        print("yes")
    else:
        print("no")

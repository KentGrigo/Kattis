def enlargeColon():
    return [" "] \
         + [" "] \
         + ["o"] \
         + [" "] \
         + ["o"] \
         + [" "] \
         + [" "]

def enlargeZero():
    return ["+---+"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+   +"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+---+"]

def enlargeOne():
    return ["    +"] \
         + ["    |"] \
         + ["    |"] \
         + ["    +"] \
         + ["    |"] \
         + ["    |"] \
         + ["    +"]

def enlargeTwo():
    return ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["+---+"] \
         + ["|    "] \
         + ["|    "] \
         + ["+---+"]

def enlargeThree():
    return ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["+---+"]

def enlargeFour():
    return ["+   +"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["    +"]

def enlargeFive():
    return ["+---+"] \
         + ["|    "] \
         + ["|    "] \
         + ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["+---+"]

def enlargeSix():
    return ["+---+"] \
         + ["|    "] \
         + ["|    "] \
         + ["+---+"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+---+"]

def enlargeSeven():
    return ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["    +"] \
         + ["    |"] \
         + ["    |"] \
         + ["    +"]

def enlargeEight():
    return ["+---+"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+---+"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+---+"]

def enlargeNine():
    return ["+---+"] \
         + ["|   |"] \
         + ["|   |"] \
         + ["+---+"] \
         + ["    |"] \
         + ["    |"] \
         + ["+---+"]

def enlargeClockPart(part):
    return {
        ":": enlargeColon(),
        "0": enlargeZero(),
        "1": enlargeOne(),
        "2": enlargeTwo(),
        "3": enlargeThree(),
        "4": enlargeFour(),
        "5": enlargeFive(),
        "6": enlargeSix(),
        "7": enlargeSeven(),
        "8": enlargeEight(),
        "9": enlargeNine(),
    }[part]

while True:
    data = input()
    if data == "end":
        break

    clockParts = list(data)
    enlargedParts = []
    for part in clockParts:
        enlargedPart = enlargeClockPart(part)
        enlargedParts.append(enlargedPart)

    height = 7
    for y in range(height):
        row = ""
        for enlargedPart in enlargedParts:
            if row != "":
                row += "  "

            enlargedPartRow = enlargedPart[y]
            row += enlargedPartRow

        print(row)

    print("")
    print("")

print("end")

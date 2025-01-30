text = input()

hasSeenSmiley = False
hasSeenFrowny = False
previousLetter = None
for letter in text:
    if previousLetter == ":" and letter == ")":
        hasSeenSmiley = True

    if previousLetter == ":" and letter == "(":
        hasSeenFrowny = True

    previousLetter = letter

if hasSeenSmiley and hasSeenFrowny:
    print("double agent")
elif hasSeenSmiley:
    print("alive")
elif hasSeenFrowny:
    print("undead")
else:
    print("machine")

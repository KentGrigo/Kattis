numberOfNotes = int(input())
notes = input().split()
staff = {}
tonesWithLedgerLines = ["a", "e", "g", "B", "D", "F"]
tones = ["a", "b", "c", "d", "e", "f", "g", "A", "B", "C", "D", "E", "F", "G"]
for tone in tones:
    staff[tone] = []

for note in notes:
    tone = note[0]
    if len(note) == 2:
        duration = int(note[1])
    else:
        duration = 1

    for staffTone in staff.keys():
        if staffTone in tonesWithLedgerLines:
            spacing = "-"
        else:
            spacing = " "

        if staffTone == tone:
            line = "*" * duration
        else:
            line = spacing * duration

        if staff[staffTone]:
            staff[staffTone].append(spacing)

        staff[staffTone].append(line)

for tone in reversed(tones):
    line = "".join(staff[tone])
    print("{}: {}".format(tone, line))

majorScalePattern = [0, 2, 2, 1, 2, 2, 2, 1]
allNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
noteToKeys = {}
for note in allNotes:
    noteToKeys[note] = set()

for index, key in enumerate(allNotes):
    for step in majorScalePattern:
        index = (index + step) % len(allNotes)
        note = allNotes[index]
        keys = noteToKeys[note]
        keys.add(key)

numberOfNotes = int(input())
notes = input().split()
possibleKeys = set(allNotes)
for note in notes:
    keys = noteToKeys[note]
    possibleKeys.intersection_update(keys)

if possibleKeys:
    print(" ".join(sorted(possibleKeys)))
else:
    print("none")

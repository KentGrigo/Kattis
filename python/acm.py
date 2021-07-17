numberOfCorrectEntries = 0
score = 0
entries = {}
while True:
    entry = input()
    if entry == "-1":
        break

    points, id, correctness = entry.split()
    idToScore = entries.get(id, 0)
    if correctness == "wrong":
        entries[id] = idToScore + 20
    else: #correctness == "right"
        score += idToScore + int(points)
        numberOfCorrectEntries += 1

print(numberOfCorrectEntries, score)

fingerings = {}
fingerings["c"] = [2, 3, 4, 7, 8, 9, 10]
fingerings["d"] = [2, 3, 4, 7, 8, 9]
fingerings["e"] = [2, 3, 4, 7, 8]
fingerings["f"] = [2, 3, 4, 7]
fingerings["g"] = [2, 3, 4]
fingerings["a"] = [2, 3]
fingerings["b"] = [2]
fingerings["C"] = [3]
fingerings["D"] = [1, 2, 3, 4, 7, 8, 9]
fingerings["E"] = [1, 2, 3, 4, 7, 8]
fingerings["F"] = [1, 2, 3, 4, 7]
fingerings["G"] = [1, 2, 3, 4]
fingerings["A"] = [1, 2, 3]
fingerings["B"] = [1, 2]

numberOfSongs = int(input())
for _ in range(numberOfSongs):
    song = input()
    numberOfPresses = {}
    numberOfPresses[1] = 0
    numberOfPresses[2] = 0
    numberOfPresses[3] = 0
    numberOfPresses[4] = 0
    numberOfPresses[5] = 0
    numberOfPresses[6] = 0
    numberOfPresses[7] = 0
    numberOfPresses[8] = 0
    numberOfPresses[9] = 0
    numberOfPresses[10] = 0

    previousFingering = []
    for note in song:
        fingering = fingerings[note]
        changes = list(set(fingering) - set(previousFingering))
        for button in changes:
            numberOfPresses[button] += 1

        previousFingering = fingering

    print(" ".join(map(str, numberOfPresses.values())))

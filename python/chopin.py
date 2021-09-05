toneToAlternative = {}
toneToAlternative["A"] = None
toneToAlternative["A#"] = "Bb"
toneToAlternative["Bb"] = "A#"
toneToAlternative["B"] = None
toneToAlternative["C"] = None
toneToAlternative["C#"] = "Db"
toneToAlternative["Db"] = "C#"
toneToAlternative["D"] = None
toneToAlternative["D#"] = "Eb"
toneToAlternative["Eb"] = "D#"
toneToAlternative["E"] = None
toneToAlternative["F"] = None
toneToAlternative["F#"] = "Gb"
toneToAlternative["Gb"] = "F#"
toneToAlternative["G"] = None
toneToAlternative["G#"] = "Ab"
toneToAlternative["Ab"] = "G#"

caseNumber = 0
while True:
    caseNumber += 1
    try:
        tone, tonality = input().split()
    except EOFError:
        break

    alternativeTone = toneToAlternative[tone]
    if alternativeTone is None:
        print("Case {}: UNIQUE".format(caseNumber))
    else:
        print("Case {}: {} {}".format(caseNumber, alternativeTone, tonality))

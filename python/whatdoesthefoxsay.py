def test():
    recordings = input().split()
    nonFoxSounds = []
    while True:
        fact = input()
        if fact == "what does the fox say?":
            break

        nonFoxSound = fact.split()[2]
        nonFoxSounds.append(nonFoxSound)
    
    foxSounds = filter(lambda sound: sound not in nonFoxSounds, recordings)
    print(" ".join(foxSounds))


numberOfTests = int(input())
for _ in range(numberOfTests):
    test()

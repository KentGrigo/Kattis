data = input().split()
numberOfLegsOnAnimal1 = int(data[0])
numberOfLegsOnAnimal2 = int(data[1])
numberOfLegsOnAnimal3 = int(data[2])
totalNumberOfLegs = int(data[3])

isPossible = False
for numberOfAnimal1 in range(251):
    legs = numberOfAnimal1 * numberOfLegsOnAnimal1
    if totalNumberOfLegs < legs:
        continue

    for numberOfAnimal2 in range(251):
        legs = numberOfAnimal1 * numberOfLegsOnAnimal1 + numberOfAnimal2 * numberOfLegsOnAnimal2
        if totalNumberOfLegs < legs:
            continue
    
        for numberOfAnimal3 in range(251):
            legs = numberOfAnimal1 * numberOfLegsOnAnimal1 + numberOfAnimal2 * numberOfLegsOnAnimal2 + numberOfAnimal3 * numberOfLegsOnAnimal3
            if totalNumberOfLegs != legs:
                continue
            
            isPossible = True
            print("{} {} {}".format(numberOfAnimal1, numberOfAnimal2, numberOfAnimal3))

if not isPossible:
    print("impossible")

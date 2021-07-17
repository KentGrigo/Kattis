def test(numberOfPeople, numberOfBeliefs, persons):
    votes = list(map(int, list("0" * numberOfBeliefs)))
    for beliefs in persons:
        for index, belief in enumerate(beliefs):
            votes[index] += int(belief)

    consensus = []
    half = numberOfPeople // 2
    for quantity in votes:
        if half < quantity:
            consensus.append(1)
        else:
            consensus.append(0)

    consensus = map(str, consensus)
    print("".join(consensus))


numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfPeople, numberOfBeliefs = list(map(int, input().split()))
    persons = []
    for _ in range(numberOfPeople):
        person = input()
        persons.append(person)
    
    test(numberOfPeople, numberOfBeliefs, persons)

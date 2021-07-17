numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfCandidates = int(input())
    sumOfVotes = 0
    maxNumberOfVotes = 0
    mostVotedCandidate = None
    for candidateNumber in range(1, numberOfCandidates + 1):
        numberOfVotes = int(input())
        sumOfVotes += numberOfVotes

        if maxNumberOfVotes == numberOfVotes:
            mostVotedCandidate = None
        elif maxNumberOfVotes < numberOfVotes:
            maxNumberOfVotes = numberOfVotes
            mostVotedCandidate = candidateNumber

    if mostVotedCandidate is None:
        print("no winner")
    else:
        half = sumOfVotes / 2
        if half < maxNumberOfVotes:
            print("majority winner {}".format(mostVotedCandidate))
        else:
            print("minority winner {}".format(mostVotedCandidate))

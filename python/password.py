numberOfPasswords = int(input())

probabilities = []
for _ in range(numberOfPasswords):
    data = input().split()
    probability = float(data[1])
    probabilities.append(probability)

probabilities.sort(reverse = True)

expectedNumberOfAttempts = 0
remainingProbability = 1.0
for probability in probabilities:
    expectedNumberOfAttempts += remainingProbability
    remainingProbability -= probability

print("{:.4f}".format(expectedNumberOfAttempts))

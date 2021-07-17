numberOfDictionaryWords, numberOfJobDescriptions = list(map(int, input().split()))
wordToEvaluation = {}
for _ in range(numberOfDictionaryWords):
    dictionaryEntry = input().split()
    word = dictionaryEntry[0]
    evaluation = int(dictionaryEntry[1])
    wordToEvaluation[word] = evaluation


for _ in range(numberOfJobDescriptions):
    jobEvaluation = 0
    while True:
        line = input()
        if line == ".":
            break

        words = line.split()
        for word in words:
            if word in wordToEvaluation:
                jobEvaluation += wordToEvaluation[word]

    print(jobEvaluation)

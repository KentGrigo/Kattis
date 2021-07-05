from typing import Hashable


def computePatternLength(sequence):
    def isPattern(patternLength):
        pattern = sequence[:patternLength]
        numberOfRepeats = sequenceLength // len(pattern) + 1
        superstring = pattern * numberOfRepeats
        return sequence in superstring

    sequenceLength = len(sequence)
    for patternLength in range(1, sequenceLength):
        if isPattern(patternLength):
            return patternLength

    return sequenceLength


numberOfTests = int(input())
for _ in range(numberOfTests):
    sequence = input()
    patternLength = computePatternLength(sequence)
    print(patternLength)

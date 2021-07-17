import re

def count(text, pattern):
    patternLength = len(pattern)
    occurrences = 0
    for textStartIndex in range(len(text)):
        textEndIndex = textStartIndex + patternLength
        textSubstring = text[textStartIndex:textEndIndex]
        if textSubstring == pattern:
            occurrences += 1

    return occurrences


while True:
    data = input()
    if data == "0":
        break

    pattern, text = data.split()
    numberOfType1 = count(text, pattern)

    type2Patterns = set()
    for index, _ in enumerate(pattern):
        type2Pattern = pattern[0:index] + pattern[index+1:]
        type2Patterns.add(type2Pattern)

    numberOfType2 = 0
    for type2Pattern in type2Patterns:
        numberOfType2 += count(text, type2Pattern)

    nucleotides = ["A", "G", "C", "T"]
    type3Patterns = set()
    for index in range(len(pattern) + 1):
        for nucleotide in nucleotides:
            type3Pattern = pattern[0:index] + nucleotide + pattern[index:]
            type3Patterns.add(type3Pattern)

    numberOfType3 = 0
    for type3Pattern in type3Patterns:
        numberOfType3 += count(text, type3Pattern)

    print(numberOfType1, numberOfType2, numberOfType3)

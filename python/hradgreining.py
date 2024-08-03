dnaSequence = input()
positiveSubsequence = "COV"
isCovPositive = positiveSubsequence in dnaSequence
if isCovPositive:
    print("Veikur!")
else:
    print("Ekki veikur!")

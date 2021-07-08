numberOfErasures = int(input())
fileBeforeDeletion = input()
fileAfterDeletion = input()

if numberOfErasures % 2 == 0:
    expectedFileAfterDeletion = fileBeforeDeletion
else:
    expectedFileAfterDeletion = fileBeforeDeletion
    expectedFileAfterDeletion = expectedFileAfterDeletion.replace("1", "2")
    expectedFileAfterDeletion = expectedFileAfterDeletion.replace("0", "1")
    expectedFileAfterDeletion = expectedFileAfterDeletion.replace("2", "0")

if fileAfterDeletion == expectedFileAfterDeletion:
    print("Deletion succeeded")
else:
    print("Deletion failed")

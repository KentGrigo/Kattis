numberOfBoatParts, numberOfDays = list(map(int, input().split()))
replacedParts = set()
dayNumberOfAllPartsReplaced = None
for dayNumber in range(1, numberOfDays + 1):
    replacedPart = input()
    replacedParts.add(replacedPart)
    if dayNumberOfAllPartsReplaced is None and len(replacedParts) == numberOfBoatParts:
        dayNumberOfAllPartsReplaced = dayNumber

if dayNumberOfAllPartsReplaced is None:
    print("paradox avoided")
else:
    print(dayNumberOfAllPartsReplaced)

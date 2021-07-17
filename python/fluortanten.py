numberOfChildren = int(input())
preferences = list(map(int, input().split()))

childNumber = 0
preferenceSumStart = 0
for preference in preferences:
    if preference == 0:
        continue

    childNumber += 1
    preferenceSumStart += childNumber * preference

preferenceSumEnd = 0
maxPreferenceSum = preferenceSumStart + preferenceSumEnd
offsetChildIndex = numberOfChildren
for preference in reversed(preferences):
    preferenceSumStart -= offsetChildIndex * preference
    preferenceSumEnd += (offsetChildIndex + 1) * preference
    offsetChildIndex -= 1
    preferenceSum = preferenceSumStart + preferenceSumEnd
    maxPreferenceSum = max(preferenceSum, maxPreferenceSum)

print(maxPreferenceSum)

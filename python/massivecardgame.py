import bisect

numberOfCards = int(input())
cards = sorted(map(int, input().split()))
minCard = cards[0]
maxCard = cards[-1]

numberOfRanges = int(input())
for _ in range(numberOfRanges):
    lowerValue, upperValue = list(map(int, input().split()))
    if maxCard < lowerValue or upperValue < minCard:
        print(0)
        continue

    lowerBound = max(minCard, lowerValue)
    upperBound = min(maxCard, upperValue)
    left = bisect.bisect_left(cards, lowerBound)
    right = bisect.bisect_right(cards, upperBound)
    count = right - left
    print(count)

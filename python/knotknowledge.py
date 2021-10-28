numberOfKnots = int(input())
knots = set(map(int, input().split()))
knownKnots = set(map(int, input().split()))
unknownKnots = knots - knownKnots
print(" ".join(map(str, unknownKnots)))

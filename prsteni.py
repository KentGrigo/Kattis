from fractions import Fraction

numberOfRings = int(input())
ringSizes = list(map(int, input().split()))
firstRingSize = ringSizes[0]
for ringSize in ringSizes[1:]:
    numberOfTurns = Fraction(firstRingSize, ringSize)
    print("{}/{}".format(numberOfTurns.numerator, numberOfTurns.denominator))

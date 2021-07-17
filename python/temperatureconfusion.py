from fractions import Fraction

data = input().split("/")
fahrenheitNumerator = int(data[0])
fahrenheitDenominator = int(data[1])

celciusNumerator = 5 * (fahrenheitNumerator - 32 * fahrenheitDenominator)
celciusDenominator = 9 * fahrenheitDenominator
reducedFraction = Fraction(celciusNumerator, celciusDenominator)

print("{}/{}".format(reducedFraction.numerator, reducedFraction.denominator))

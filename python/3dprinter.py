import math

numberOfStatuesToBePrinted = int(input())
numberOfDays = math.ceil(math.log(numberOfStatuesToBePrinted, 2)) + 1
print(numberOfDays)

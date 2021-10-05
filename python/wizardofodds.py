import math

endRange, numberOfGuesses = list(map(int, input().split()))
numberOfGuessesNeeded = math.log2(endRange)
if numberOfGuessesNeeded <= numberOfGuesses:
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")

numberOfNumbers = int(input())
firstNumberOfRound = None
for _ in range(numberOfNumbers):
    number = int(input())
    if firstNumberOfRound is None:
        firstNumberOfRound = number
    elif number % firstNumberOfRound == 0:
        print(number)
        firstNumberOfRound = None

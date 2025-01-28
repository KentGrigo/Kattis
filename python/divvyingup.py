numberOfContests = int(input())
prizes = list(map(int, input().split()))
total = sum(prizes)
canBeSplitEqually = total % 3 == 0
if canBeSplitEqually:
    print("yes")
else:
    print("no")

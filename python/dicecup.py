data = input().split()
die1 = int(data[0])
die2 = int(data[1])

minimum = min(die1, die2)
maximum = max(die1, die2)

for value in range(minimum + 1, maximum + 2):
    print(value)
def parse(value1, value2):
    if value1.isnumeric():
        color = value2
        diameter = int(value1)
    else:
        color = value1
        diameter = int(value2) * 2

    return (diameter, color)


numberOfCups = int(input())
cups = []
for _ in range(numberOfCups):
    cup = parse(*input().split())
    cups.append(cup)

cups.sort()
for _, color in cups:
    print(color)

sideLength = int(input())
topAndBottom = '+' + sideLength * '-' + '+'
side = '|' + sideLength * ' ' + '|'

print(topAndBottom)
for _ in range(sideLength):
    print(side)

print(topAndBottom)

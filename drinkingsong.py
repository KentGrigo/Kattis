numberOfBottles = int(input())
beverage = input()

for bottlesLeft in range(numberOfBottles, 2, -1):
    print("{0} bottles of {1} on the wall, {0} bottles of {1}.".format(bottlesLeft, beverage))
    print("Take one down, pass it around, {0} bottles of {1} on the wall.".format(bottlesLeft - 1, beverage))
    print("")

if 1 < numberOfBottles:
    print("2 bottles of {0} on the wall, 2 bottles of {0}.".format(beverage))
    print("Take one down, pass it around, 1 bottle of {0} on the wall.".format(beverage))
    print("")

print("1 bottle of {0} on the wall, 1 bottle of {0}.".format(beverage))
print("Take it down, pass it around, no more bottles of {0}.".format(beverage))

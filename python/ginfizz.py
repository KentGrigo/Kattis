numberOfDrinks = int(input())

amountOfGin = 45 * numberOfDrinks
amountOfLemonJuice = 30 * numberOfDrinks
amountOfSyrup = 10 * numberOfDrinks
numberOfLemonSlices = numberOfDrinks
pluralS = "s" if 1 < numberOfLemonSlices else ""

print(f"{amountOfGin} ml gin")
print(f"{amountOfLemonJuice} ml fresh lemon juice")
print(f"{amountOfSyrup} ml simple syrup")
print(f"{numberOfLemonSlices} slice{pluralS} of lemon")

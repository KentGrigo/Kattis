numberOfAnimals = int(input())
binaryNumber = ""
for _ in range(numberOfAnimals):
    animal = input()
    if animal == "Z":
        binaryNumber += "0"
    else:
        binaryNumber += "1"

decimal = int(binaryNumber, 2)
print(decimal)

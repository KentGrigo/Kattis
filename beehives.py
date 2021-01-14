import math

class Hive:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(hive1, hive2):
    diffX = hive1.x - hive2.x
    diffY = hive1.y - hive2.y
    return math.sqrt(diffX ** 2 + diffY ** 2)

def removeIfExists(element, collection):
    if element in collection:
        collection.remove(element)

def test(fightingRange, hives):
    sweetHives = hives.copy()
    for index1 in range(len(hives)):
        hive1 = hives[index1]
        for index2 in range(index1):
            hive2 = hives[index2]
            hiveDistance = distance(hive1, hive2)
            if hiveDistance <= fightingRange:
                removeIfExists(hive1, sweetHives)
                removeIfExists(hive2, sweetHives)

    numberOfSweetHives = len(sweetHives)
    numberOfSourHives = len(hives) - numberOfSweetHives
    print("{} sour, {} sweet".format(numberOfSourHives, numberOfSweetHives))


while True:
    data = input().split()
    fightingRange = float(data[0])
    numberOfHives = int(data[1])
    if fightingRange == 0.0 and numberOfHives == 0:
        break

    hives = []
    for _ in range(numberOfHives):
        hive = Hive(*list(map(float, input().split())))
        hives.append(hive)

    test(fightingRange, hives)

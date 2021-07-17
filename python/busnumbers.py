def representCollection(collection):
    numberOfBusses = len(collection)
    if numberOfBusses == 0:
        return ""
    elif numberOfBusses == 1:
        return str(collection[0])
    elif numberOfBusses == 2:
        return "{} {}".format(collection[0], collection[1])
    else:
        return "{}-{}".format(collection[0], collection[-1])


numberOfBusses = int(input())
busses = list(map(int, input().split()))
busses.sort()

collections = []
currentCollection = []
previousBus = None
for currentBus in busses:
    if previousBus is None:
        currentCollection.append(currentBus)
    else:
        if previousBus + 1 == currentBus:
            currentCollection.append(currentBus)
        else:
            collections.append(currentCollection)
            currentCollection = []
            currentCollection.append(currentBus)

    previousBus = currentBus

if currentCollection:
    collections.append(currentCollection)
    currentCollection = []

representation = ""
for collection in collections:
    if representation != "":
        representation += " "

    representation += representCollection(collection)

print(representation)

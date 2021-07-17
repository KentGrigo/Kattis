def test():
    numberOfShipments = int(input())
    toyToQuantity = {}
    for _ in range(numberOfShipments):
        shipment = input().split()
        toy = shipment[0]
        quantity = int(shipment[1])
        previousQuantity = toyToQuantity.get(toy, 0)
        toyToQuantity[toy] = previousQuantity + quantity

    toyToQuantity = {toy: quantity for toy, quantity in sorted(toyToQuantity.items(), key = lambda item: (-item[1], item[0]))}
    print(len(toyToQuantity))
    for (toy, quantity) in toyToQuantity.items():
        print("{} {}".format(toy, quantity))


numberOfTests = int(input())
for _ in range(numberOfTests):
    test()

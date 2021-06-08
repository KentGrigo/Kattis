numberOfItems, numberOfPicksAlice, numberOfPicksBob, numberOfPicksClara = list(map(int, input().split()))
isPossibleToOrderDifferent = numberOfPicksAlice + numberOfPicksBob + numberOfPicksClara <= 2 * numberOfItems
if isPossibleToOrderDifferent:
    print("possible")
else:
    print("impossible")

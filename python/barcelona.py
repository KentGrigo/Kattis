numberOfBags, bennysBag = list(map(int, input().split()))
bags = list(map(int, input().split()))
positionOfBennysBag = bags.index(bennysBag)
if positionOfBennysBag == 0:
    print("fyrst")
elif positionOfBennysBag == 1:
    print("naestfyrst")
else:
    print(f"{positionOfBennysBag + 1} fyrst")
